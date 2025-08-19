from dataclasses import dataclass


# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def __repr__(self) -> str:
#         return f"Person(name={self.name}, age={self.age})"

#     def __str__(self) -> str:
#         return f"Person: {self.name}, Age: {self.age}"

#     def get_name(self) -> str:
#         return self.name


@dataclass
class Person:
    name: str
    age: int
    salary: float = 0.0

    def get_name(self) -> str:
        return self.name


person = Person("John", 30, 1000.0)
print(person.name)
print(person.age)
print(person.salary)
print(person.get_name())


# @dataclass
# class Payment:
#     amount: float
#     date: str
#     description: str = "Payment"
#     person: Person = Person("John", 30, 1000.0)


# def money_count(payment: Payment) -> float:
#     return payment.amount + 2000