# def temperature(a, b, c, d):
#     my_temp = (a - b) * c/d
#     return my_temp

# celsius=temperature (100, 32, 5, 9) 
# print(celsius)

# REMADE

def temp (Fahrenheit: float, num_2 = 32, num_3 = 5, num_4 = 9) -> float:
    my_celsius = (Fahrenheit - num_2) * num_3 / num_4
    return my_celsius

temperature=temp(22.3)
print(temperature)

# CALCULATOR

def calc(num_1: float, num_2: float = 55.5) -> float:
    my_calc1 = num_1 + num_2
    my_calc2 = num_1 - num_2
    my_calc3 = num_1 / num_2
    my_calc4 = num_1 ** num_2
    return my_calc1, my_calc2, my_calc3, my_calc4

values = calc(10)
print(values)

# Calculate average speed in meters/sec .Distance is given in Km and time in hours.

def speed (kmh: int , num_2 = 5, num_3 = 18) -> int:
    ms = kmh * num_2 / num_3
    return ms 

spped=speed(100)
print(spped)
