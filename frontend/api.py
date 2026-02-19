import requests
from utils import check_payload
BASE_URL = "http://localhost:6969"

def generate_ideas(payload:dict) -> requests.Response:
    payload = check_payload(payload)
    response = requests.post(f"{BASE_URL}/generate",json=payload)
    return response

def discuss_ideas(payload:dict) -> requests.Response:
    payload = check_payload(payload)
    respose = requests.post(f"{BASE_URL}/discuss",json=payload)
    return respose