# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

#     def get_name(self) -> str:
#         return self.name

#     @staticmethod
#     def calculate_birth_year(age: int) -> int:
#         return 2025 - age
    
#     @classmethod
#     def from_birth_year(cls, birth_year: int) -> int:
#         age = 2025 - birth_year
#         return age

#     @classmethod
#     def init_person(cls, age: int) -> "Person":
#         age_year = cls.calculate_birth_year(age)
#         # doing smth before

#         return cls("John", age=age_year) # return Person("John", 30)


# my_person = Person("Antanas", 30)
# my_second_person = Person.init_person()
# print(my_person.get_name())
# print(my_second_person.get_name())


# class Point:
#     def __init__(self, x: float, y: float):
#         self.x = x
#         self.y = y

#     @classmethod
#     def from_tuple(cls, point_tuple: tuple[float, float]) -> "Point":
#         x, y = point_tuple
#         return cls(x, y)


# point: Point = Point.from_tuple((3, 4))
# print(point.x)  # 3
# print(point.y)  # 4

# import datetime


# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name: str, birth_year: int) -> "Person":
#         age = cls.get_age(birth_year)
#         return cls(name, age)

#     @staticmethod
#     def get_age(birth_year: int) -> int:
#         return datetime.date.today().year - birth_year


# person: Person = Person.from_birth_year("John", 1990)
# print(person.name)  # John
# print(person.age)  # 33


¬

class Fridge:
    def __init__(self, door: int, capasity: float, cooling_temp: float, color: str):
        self.door = door
        self.capasity = capasity
        self.cooling_temp = cooling_temp
        self.color = color

    def door_count(self):
        return 60
        

class home_fridge(Fridge):

    def fridge_capasity(self):
        return "2m2"

class school_fridge(Fridge):

    def temp_cool(self):
        return "temperature is +4 C"

class work_fridge(Fridge):

    def what_color(self):
        return "White"
    
@classmethod
    
def all_fridge_color(self):
    fridge_color = "purple"
    return fridge_color

@classmethod

def all_fridge_temp(self):
    fridge_temp = "-100"
    return fridge_temp

fridge = Fridge()
print(fridge.fridge_capasity())