# Leiskite vartotojui įvesti 10 sveikųjų skaičių, tada atspausdinkite šių skaičių sumą ir vidurkį.


total_sum = 0

for i in range(10):
    number = int(input(f"Įveskite sveikąjį skaičių {i + 1}: "))
    total_sum += number
    
average = total_sum / 10
print(f"Suma: {total_sum}, Vidurkis: {average}")