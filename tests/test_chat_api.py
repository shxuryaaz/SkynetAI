import requests

def test_chat_api():
    url = "http://127.0.0.1:8000/chat/"
    payload = {"query": "What is finance?", "domain": "finance"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    print("Test response:", response.json())
