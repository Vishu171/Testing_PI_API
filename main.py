import streamlit as st
import openai
import json
import requests

# Set OpenAI API key
openai.api_key = st.secrets["openai_key"]

def get_product_info(query):
    query_json = json.dumps({"query": query})
    
    # Replace this with your actual API URL
    api_url = "https://www.power.com/jsonapi/node/document"
    response = requests.post(api_url, data=query_json)
    api_response = response.json()

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Tell me about the configuration of {query}"},
            {"role": "assistant", "content": str(api_response)}
        ]
    )
    return completion.choices[0].message['content']

st.title("Product Information Assistant")

query = st.text_input("Enter your product query:")
if st.button("Get Product Info"):
    if query:
        product_info = get_product_info(query)
        st.write(product_info)
    else:
        st.write("Please enter a query to get information.")
