# 🛡️ GuardOps: Secure RAG Architecture with Security Middleware

An enterprise-grade, 3-tier microservice implementation designed to protect Retrieval-Augmented Generation (RAG) pipelines against prompt injections and sensitive data exfiltration leaks.

## 🏗️ Architecture Design
The ecosystem is decoupled into three independent microservices to ensure modular scalability and a minimal attack surface:
1. **The Core Engine (Port 8000):** FastAPI backend communicating securely with OpenAI APIs to process standard semantic payloads.
2. **The Security Proxy (Port 8001):** Middleware boundary scanning inbound prompts for adversarial manipulation and outbound vectors for cryptographic data leaks.
3. **The User Interface (Port 8501):** Streamlit conversational chat module.

## 🚀 How to Run Locally
1. Clone the repository and navigate inside:
   ```bash
   git clone [https://github.com/LanreOyeleke/GuardOps-Secure-RAG.git](https://github.com/LanreOyeleke/GuardOps-Secure-RAG.git)
   cd GuardOps-Secure-RAG
  set OPENAI_API_KEY=your_key_here 
