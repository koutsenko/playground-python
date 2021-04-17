import requests


def request_local(login, password):
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200


def request_local_secure(login, password):
    response = requests.post('http://127.0.0.1:4000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200
