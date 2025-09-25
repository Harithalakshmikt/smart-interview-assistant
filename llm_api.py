import requests

def call_llm_api(prompt):
    headers = {"Authorization": "Bearer your_hf_token"}  # Replace with your token
    payload = {"inputs": prompt}

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        result = response.json()

        # Handle both list and dict formats
        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"]
        else:
            return "❌ No valid response from model."

    except Exception as e:
        return f"❌ API Error: {str(e)}"
