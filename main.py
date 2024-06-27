import requests


def post_items(username: str, email: str, password: str):
    url = 'http://127.0.0.1:8000/register/'
    data = {
        "username": username,
        "email": email,
        "password": password
    }
    response = requests.post(url, json=data)
    return response.status_code, response.json()


def get_items():
    url = "http://127.0.0.1:8000/data/"
    response = requests.get(url)
    return response.status_code, response.json()


post_items("azizbekrahimjonv", "azizbekrahimjonov571@gmail.com", "admin123")
print(get_items())
