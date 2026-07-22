import requests

URL = "https://jsonplaceholder.typicode.com/users/1"


def get_user() -> dict:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()
