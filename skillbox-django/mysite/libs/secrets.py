import json

SECRETS = {}


def load(path):
    global SECRETS
    try:
        with open(path, 'r') as f:
            SECRETS = json.loads(f.read())
    except Exception as E:
        print(f'Load secrets.json error: {E}')


def get(value, default=None):
    return SECRETS.get(value, default)
