
class transport:
    def __init__(self, color):
        self.color = color

    def transport_class(self) -> str:
        return "crashed"
            

    def number_of_wheels(self) -> int:
        return "20"

    def color(self) -> str:
        return self.color
    
    def manufacturer(self) -> str:
        return "Rols Royce"

class car(transport):

    def __init__(self, color):
        self.bus_color = color
        super().__init__(color=color)
        
    def manufacturer(self) -> str:
        return "MAZDA"
    def color(self) -> str:
        return "PINKRED"
    def number_of_weels(self) -> str:
        return "666" 

class boat(transport):

    def __init__(self, color):
        self.bus_color = color
        super().__init__(color=color)
    
    def manufacturer(self) -> str:
        return "YACHT"
    def color(self) -> str:
        return "RED"
    def type(self) -> str:
        return "SUNKEN"

class plane(transport):
             
    def __init__(self, color):
        self.plane_color = "red"
        super().__init__(color=color)

    def manufacturer(self) -> str:
        return "CESNA"
    def color(self) -> str:
        return "pink"
    def type(self) -> str:
        return "CRASHED"

my_plane = plane ("pink") 
print(my_plane.number_of_wheels())
print(my_plane.transport_class())
print(my_plane.manufacturer())
print(my_plane.color)