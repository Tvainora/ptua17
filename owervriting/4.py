
class Shape:
    def __init__(self, name: str, sides: int):
        self.name = name
        self.sides = sides

    def area(self) -> float:
        pass



class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle", 4)
        self.width = width
        self.height = height

    def area(self) -> float:
         return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_lenght: float):
        super().__init__(side_lenght, side_lenght)
        self.side_lenght = side_lenght

square = Square(5)
print(square.name)
print(square.sides)  
print(square.area()) 