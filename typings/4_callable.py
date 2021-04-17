from collections.abc import Callable


def calc_and_print(calc: Callable[[int], bool], number: int) -> None:
    print(calc(number))


def is_odd(number: int) -> bool:
    return True if (number % 2) == 0 else False


calc_and_print(is_odd, 2)
