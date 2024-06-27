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

def delete_items(id: int):
    url = f'http://127.0.0.1:8000/delete/{id}/'

    response = requests.delete(url)
    return response.status_code


print(get_items())

