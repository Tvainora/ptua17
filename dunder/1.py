# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def __repr__(self) -> str:
#         return f"Person(name={self.name}, age={self.age})"

#     def __str__(self) -> str:
#         return f"Person: {self.name}, Age: {self.age}"

#     def __eq__(self, other: "Person"):
#         if isinstance(other, Person):
#             return self.name == other.name and self.age == other.age
#         return False

#     def __len__(self) -> int:
#         return len(self.name)

#     # def get_name(self) -> str:
#     #     return self.name


# my_person_uno = Person("Antanas", 30)
# my_person_duos = Person("Antanas", 30)
# my_person_tres = Person("Petras", 30)

# print(len(my_person_uno))



class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price})"

    def __str__(self) -> str:
        return f"Product: {self.name}, Price: {self.price}"

my_product = Product("Laptop", 1500.0)
my_product_2 = Product("Headfones", 991500.0)
print(repr(my_product))
print(str(my_product))
print(repr(my_product_2))
print(str(my_product_2))
