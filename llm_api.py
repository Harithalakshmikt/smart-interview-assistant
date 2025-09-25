import requests

def call_llm_api(prompt):
    headers = {"Authorization": "Bearer your_hf_token"}  # Replace with your token
    payload = {"inputs": prompt}
    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
        headers=headers,
        json=payload
    )
    return response.json()[0]["generated_text"]
