#!/usr/bin/env python3

import requests
from threading import Thread
import time

sites = [
    'http://www.google.com',
    'http://habr.com',
    'http://vk.com',
    'http://fb.com',
    'http://www.gmail.com',
]
reqs_per_site = 100
# alphabet = '0123456789abcdef'
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)


def request(site, tryout):
    try:
        response = requests.get(site)
        print('№', tryout, 'GET', site, response.status_code,
              len(response.text), 'bytes')
    except:
        print('№', tryout, 'GET', site, 'something get wrong')


def main():
    # for site in sites:
    #     for tryout in range(1, reqs_per_site+1):
    #         Thread(target=request, args=(site, tryout)).start()

    # 1000 // 16 = 62
    # 1000 % 16 = 8
    # 62 * 16 + 8 = 1000

    i = 0
    length = 0

    while True:
        password = ''
        temp = i
        while temp > 0:
            c = temp // base
            r = temp % base
            password = alphabet[r] + password
            temp = c
            # time.sleep(1)

        if (len(password) < length):
            zeros_count = length - len(password)
            password = alphabet[0] * zeros_count + password

        # test password
        print('length', length, i, password)

        # request
        response = requests.post(
            'http://127.0.0.1:5000/auth', json={'login': 'cat', 'password': password})
        if response.status_code == 200:
            print('SUCCESS', password)
            break

        # password
        if password.count(alphabet[-1]) == length:
            length += 1
            i = 0
        else:
            i += 1


if __name__ == '__main__':
    main()
