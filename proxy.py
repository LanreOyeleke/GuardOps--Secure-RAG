from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="Security Bouncer Proxy")

class QueryRequest(BaseModel):
    user_prompt: str

# Words we want to block
DANGEROUS_INPUTS = ["override", "ignore", "system administrator", "key"]
SENSITIVE_OUTPUTS = ["SECRET_NEMESIS", "10.240.", "API_KEY", "P@ssword123"]

@app.post("/secure-query")
async def secure_query(request: QueryRequest):
    # INBOUND CHECK
    prompt_lower = request.user_prompt.lower()
    if any(word in prompt_lower for word in DANGEROUS_INPUTS):
        raise HTTPException(status_code=403, detail="Bouncer: Malicious input detected!")
    
    # FORWARD TO STEP 1 APP
    try:
        step_1_url = "http://localhost:8000/query"
        main_app_response = requests.post(step_1_url, json={"user_prompt": request.user_prompt})
        llm_answer = main_app_response.json().get("answer", "")
    except Exception:
        raise HTTPException(status_code=500, detail="Could not reach the main RAG application.")
    
    # OUTBOUND CHECK
    if any(word in llm_answer for word in SENSITIVE_OUTPUTS):
        raise HTTPException(status_code=500, detail="Bouncer: Sensitive data leak prevented!")
        
    return {"answer": llm_answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)