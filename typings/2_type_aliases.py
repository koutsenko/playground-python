from typing import Any, Union


# Тип данных 0 - строка или число
StrOrInt = Union[int, str]
t0_var1: StrOrInt = 'my_string'
t0_var2: StrOrInt = 5
t0_var_err1: StrOrInt = None
print(t0_var1)
print(t0_var2)
print(t0_var_err1)

# Тип данных 1 - кортеж c 3 элементами
TupleThreeElements = tuple[Any, Any, Any]

t1_var1: TupleThreeElements = (0, "any element", None)
t1_var_err1: TupleThreeElements = (False, 5)
print(t1_var1)
print(t1_var_err1)

# Тип данных 2 - кортеж с 2 элементами (строка и число)
TupleTwoElementsStrInt = tuple[str, int]

t2_var1: TupleTwoElementsStrInt = ('hello', 5)
t2_var_err1: TupleTwoElementsStrInt = ('bad', 'initialization', 5)
t2_var_err2: TupleTwoElementsStrInt = (False, None, 'shit')
t2_var_err3: TupleTwoElementsStrInt = (False, False)
print(t2_var1)
print(t2_var_err1)
print(t2_var_err2)
print(t2_var_err3)

# Тип данных 3 - кортеж с неограниченным кол-вом чисел
TupleInt = tuple[int, ...]

t3_var1: TupleInt = (1, 2, 3, 4, 5, 6)
t3_var2: TupleInt = (1,)
t3_var_err1: TupleInt = ("string", 2, 5)
print(t3_var1)
print(t3_var2)
print(t3_var_err1)

# Тип данных 4 - кортеж в котором могут быть либо числа, либо строки
TupleIntOrString = tuple[Union[int, str], ...]

t4_var1: TupleIntOrString = ('string1', 1, 24)
t4_var2: TupleIntOrString = (0, )
t4_err1: TupleIntOrString = (None, False, 'string1')
print(t4_var1)
print(t4_var2)
print(t4_err1)
