from typing import NewType


# Декларация нового типа "UserId"
UserId = NewType('UserId', int)


def odd_or_even(user_id: UserId) -> str:
    return 'odd' if (user_id % 2) == 0 else 'even'


some_id = UserId(5423434)
some_id_wrong = -1
print(odd_or_even(some_id))
print(odd_or_even(some_id_wrong))

# # Сложение двух UserId вернет int
output = UserId(23413) + UserId(54341)
print(output)

# Производный тип данных
ProUserId = NewType('ProUserId', UserId)
some_id_2 = ProUserId(UserId(5))
print(some_id_2)
