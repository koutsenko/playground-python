with open('10-million-password-list-top-1000000.txt') as f:
    content = f.read()
passwords = content.split('\n')


def popular_password(state):
    if state is None:
        state = 0

    if state >= len(passwords) - 1:
        next_state = None
    else:
        next_state = state + 1

    return passwords[state], next_state


logins = ['admin', 'jack', 'cat']


def simple_logins(state):
    if state is None:
        state = 0

    if state >= len(logins) - 1:
        next_state = None
    else:
        next_state = state + 1

    return logins[state], next_state


alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)


def brute_force(state):
    if state is None:
        state = 0, 0
    i, length = state

    # i: 10 -> base
    password = ''
    temp = i
    while temp > 0:
        c = temp // base
        r = temp % base
        password = alphabet[r] + password
        temp = c

    if len(password) < length:
        zeros_count = length - len(password)
        password = alphabet[0] * zeros_count + password

    # next state
    if password.count(alphabet[-1]) == length:
        length += 1
        i = 0
    else:
        i += 1
    next_state = i, length

    return password, next_state
