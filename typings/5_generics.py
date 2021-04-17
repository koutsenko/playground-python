from collections.abc import Mapping, Sequence
from typing import TypeVar


Employee = tuple[str, str, str]
EmployeesMutable = list[Employee]
EmployeesImmutable = tuple[Employee, ...]
EmployeesById = dict[str, Employee]


# Печать фамилий в последовательности работников.
# Вместо конкретного типа списка, указан дженерик-алиас для всех типов списков.
def print_surnames(employees: Sequence[Employee]) -> None:
    for employee in employees:
        print(employee[0])  


man1: Employee = ('Kutsenko', 'Dmitry', 'Sergeeevich')
man2: Employee = ('Peskov', 'Dmitry', 'Sergeevich')
man3: Employee = ('Putin', 'Vladimir', 'Vladimirovich')
people1: EmployeesMutable = [man1, man2, man3]
people2: EmployeesImmutable = (man1, man2, man3)
print_surnames(people1)
print_surnames(people2)


# Напечатаем фамилии и ID работников.
# Вместо конкретного типа словаря, указан дженерик-алиас для всех типов словарей.
def print_surnames_map(employees: Mapping[str, Employee]) -> None:
    for k, v in employees.items():
        print(k, v[0])


people_by_id: EmployeesById = {
    'fj3ogib8d': man1,
    'fg9sj3kgi': man2,
    'zvb93kfug': man3,
}
print_surnames_map(people_by_id)


T = TypeVar('T') 


# Вернем первую запись в списке работников.
# Вернется элемент того же типа, как и во входном списке.
def first(employees: Sequence[T]) -> T:
    return employees[0]


print(first(people1)[0])
