import streamlit as st
import requests

# Set up the page
st.set_page_config(page_title="Project Nemesis", page_icon="🛡️")
st.title("🛡️ Project Nemesis Secure Chat")
st.write("Welcome to the secure portal. All inputs are monitored.")

# Create the chat input
user_input = st.text_input("Ask the AI a question:")

# Create the send button
if st.button("Send"):
    if user_input:
        with st.spinner("Analyzing request..."):
            try:
                # We send the request to the BOUNCER (Port 8001), not the main brain!
                proxy_url = "http://localhost:8001/secure-query"
                response = requests.post(proxy_url, json={"user_prompt": user_input})
                
                # Check if it was successful or blocked
                if response.status_code == 200:
                    st.success("🤖 " + response.json()["answer"])
                else:
                    st.error(f"🚨 SECURITY INTERVENTION: {response.json()['detail']}")
                    
            except Exception:
                st.error("Error: Could not connect to the security proxy.")