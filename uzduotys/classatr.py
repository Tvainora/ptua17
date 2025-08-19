class Animal:
    # Encapsulation: Protected attribute
    def __init__(self, name):
        self._name = name

    def speak(self):
        return f"{self._name} makes a sound."

    # Property with getter, setter, and deleter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


class Dog(Animal):
    # Polymorphism: Overriding the speak method
    def speak(self):
        return f"{self._name} barks."


class Cat(Animal):
    # Polymorphism: Overriding the speak method
    def speak(self):
        return f"{self._name} meows."


class AnimalUtils:
    # Static method
    @staticmethod
    def is_animal(obj):
        return isinstance(obj, Animal)

    # Class method
    @classmethod
    def create_dog(cls, name):
        return Dog(name)


# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy barks.
print(cat.speak())  # Whiskers meows.

# Using property
dog.name = "Max"
print(dog.name)  # Max
del dog.name

# Using static and class methods
print(AnimalUtils.is_animal(dog))  # True
new_dog = AnimalUtils.create_dog("Charlie")
print(new_dog.speak())  # Charlie barks.
