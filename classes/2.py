class Evaporator:

    def __init__(self, brand, age, price, size, power):
        self.brand = brand 
        self.year = age
        self.price = price
        self.price = size
        self.price = power
        self.name = 'Cooling unit'

    # class instance method
    
    def get_brand(self):
        return self.brand
    
    def get_age(self):
        return 2025 - self.age

    def get_price(self):
        return self.price
    
    def get_brand(self):
        return self.brand
    
    def get_size(self):
        return self.size
    
    def get_power(self):
        return self.power 

#     def create_report(self):
#         return f"Brand: {self.brand}, Year: {self.year}, Price: {self.price}, Size: {self.size}, Power: {self.power}"
    


# evp1 = Evaporator(brand="REFRA", age=2015, price=9000, size=2, power=9000)
# evp2 = Evaporator(brand="DANFOSS", age=2018, price=69999, size=10, power=80000)
# evp2 = Evaporator(brand="INDEX", age=2012, price=6, size=1, power=100)
# evp2 = Evaporator(brand="MDS", age=2025, price=9000, size= 4, power=400)
# evp2 = Evaporator(brand="COOLAID", age=2020, price=15000, size= 8, power=50000)


# print(Evaporator.create_report(self="UNIT"))
# print(Evaporator.get_brand())
# print(Evaporator.get_age())
# print(Evaporator.get_price())
# print(Evaporator.get_size())
# print(Evaporator.get_power())