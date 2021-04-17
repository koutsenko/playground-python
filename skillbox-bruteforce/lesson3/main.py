#!/usr/bin/env python3


import logic
import generators
import queries


# logic.one_login_logic(
#     login_generator=generators.simple_logins,
#     password_generator=generators.popular_password,
#     query=queries.request_local
# )


# logic.try_many_logins_logic(
#     login_generator=generators.simple_logins,
#     password_generator=generators.brute_force,
#     query=queries.request_local
# )


logic.try_many_logins_2_logic(
    login_generator=generators.simple_logins,
    password_generator=generators.brute_force,
    query=queries.request_local
)
