import requests

API_URL = "https://e24b-34-124-248-69.ngrok-free.app/chat"

def preguntar(prompt):
    response = requests.post(API_URL, json={"prompt": prompt})
    return response.json()["response"]
