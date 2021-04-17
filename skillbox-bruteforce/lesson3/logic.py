
def one_login_logic(login_generator, password_generator, query):
    login, next_login_state = login_generator(None)

    next_password_state = None
    while True:
        password, next_password_state = password_generator(next_password_state)

        if query(login, password):
            print('SUCCESS', login, password)
            break

        if next_password_state is None:
            break


def try_many_logins_logic(login_generator, password_generator, query):
    '''Использует те пароли которые даже уже подобрали...'''
    next_password_state = None
    while True:
        password, next_password_state = password_generator(next_password_state)

        next_login_state = None
        while True:
            login, next_login_state = login_generator(next_login_state)

            if query(login, password):
                print('SUCCESS', login, password)
                break

            if next_login_state is None:
                break

        if next_password_state is None:
            break


def try_many_logins_2_logic(login_generator, password_generator, query):
    password_limit = 100000
    next_login_state = None
    while True:
        login, next_login_state = login_generator(next_login_state)

        next_password_state = None
        for i in range(password_limit):
            password, next_password_state = password_generator(next_password_state)

            if query(login, password):
                print('SUCCESS', login, password)
                break

            if next_password_state is None:
                break

        if next_login_state is None:
            break
