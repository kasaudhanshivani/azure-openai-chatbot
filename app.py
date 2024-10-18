import streamlit as st
import requests
import json

def main():
    st.title("Azure OpenAI GPT-4o Connectivity Test")

    azure_openai_key = "22ec84421ec24230a3638d1b51e3a7dc"  
    azure_openai_endpoint = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"  

    user_input = st.text_input("You: ", "")

    if st.button("Send"):
        if user_input:
            try:
                headers = {
                    "Content-Type": "application/json",
                    "api-key": azure_openai_key
                }

                data = {
                    "messages": [{"role": "user", "content": user_input}],
                    "max_tokens": 50
                }

                with st.spinner("Getting response from Azure..."):
                    response = requests.post(azure_openai_endpoint, headers=headers, json=data)

                if response.status_code == 200:
                    result = response.json()
                    st.success(result["choices"][0]["message"]["content"].strip())
                else:
                    st.error(f"Failed to connect or retrieve response: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Failed to connect or retrieve response: {str(e)}")
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
