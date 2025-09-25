import requests

def search_web(query):
    params = {
        "q": query,
        "num": 5,
        "api_key": "your_serpapi_key"  # Replace with your actual key
    }
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json().get("organic_results", [])
    return [r["snippet"] for r in results if "snippet" in r]
