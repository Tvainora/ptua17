# class A:
#     def __init__(self):
#         pass

#     def start(self) -> None:
#         print("Starting A...")
    
#     def stop(self) -> None:
#         print("Stopping A...")

#     @staticmethod
#     def len_string(string: str) -> int:
#         return len(string)
    
#     def smth(value:str) -> None:
#         A.len_string(value)
        

    




# my_class = A()
# my_class.start()
# my_class.stop()
# print(my_class.len_string("Hello"))

# print(A.len_string("Hello"))


class Temp:
    def __init__ (self, kelvin):
        self.kelvin = kelvin



    @staticmethod
    def celsius(kelvin):
        return round(kelvin - 273.15)
    if celsius <= 0:
            print("Minimum kelvin is 0")
    
    @staticmethod
    def fahrenheit(kelvin):
        return round((kelvin - 273.15) * 9/5 + 32)
    if fahrenheit <= 0:
            print("Minimum kelvin is 0")


print(Temp.celsius(0))
print(Temp.fahrenheit(0))

