# Sukurkite klasę Person, kuri turi du metodus: set_name ir set_age, kuriais nustatomi atitinkamai klasės vardo ir amžiaus atributai. 
# Pakeiskite šiuos metodus taip, kad jie grąžintų self, kad juos būtų galima iškviesti grandininiu būdu.


# class Person:

#     def __init__(self):
#         self.name = None
#         self.age = None

#     def set_name(self, name: str) -> "Person":
#         self.name = name
#         return self

#     def set_age(self, age: int) -> "Person":
#         self.age = age
#         return self

# person = Person()
# person.set_name("Neimantas").set_age(99)
# print(person.name)
# print(person.age)


# Sukurkite Animal klasę su metodu speak, kuris spausdina „Animal can't speak“ (gyvūnas negali kalbėti).

# Sukurkite klasę Dog, kuri paveldi iš Animal ir pakeičia metodą speak, kad spausdintų „Woof woof“.

# Sukurkite klasę Cat, kuri paveldi Animalklasę ir pakeičia speak metodą . Tačiau šiame naujame metode iškvieskite klasės Animal metodą speak naudodami 
# super() funkciją, po to spausdinkite „Meow meow“.

class Animals:
    def speak(self):
        return "Unfortunatly but animals cant speak"
    
class Dog(Animals):
    def speak (self):
        return "woof woof"
    
class Cat(Animals):
    def speak (self):
        super().speak()
        return "mew mew"

old_dog = Dog()
print(old_dog.speak())
new_cat = Cat()
print(new_cat.speak())


