
class Moto:
    def __init__(moto, brand, year, price, tires):
        moto.brand = brand 
        moto.year = year
        moto.price = price
        moto.price = tires
        moto.name = 'Birbyne'

    def get_brand(moto):
        return moto.brand
    
    def get_year(moto):
        return 2025-moto.year
    
    def get_price(moto):
        return moto.price
    
    def get_tires(moto):
        return moto.tires
    
    def create_report(moto):
        return f"Brand: {moto.brand}, Year: {moto.year}, Price: {moto.price}, Tire Count {moto.tires}"
    
    moto1 = (brand="Suzuki", Year=2015, price=2000, tire_count=2)
    print(Moto(brand="Suzuki", year=2015, price=10000, tires=7))
    print(moto.get_brand)
    print(moto.get_year)
    print(moto.get_price)
    print(moto.get_tires)

