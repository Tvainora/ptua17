# Leiskite vartotojui įvesti du skaičius. Atspausdinkite, kuris iš jų yra didesnis, arba praneškite, kad skaičiai yra lygūs, jei taip yra.

num1 = float(input("Pirmas skaicius: "))
num2 = float(input("Antras skaicius: "))

if num1 > num2:
    print(f"Pirmas skaicius didesnis {num1}")
elif num1 == num2:
        print(f"Skaiciai yra lygus {num1} = {num2}")
else:
    print(f"Antras skaicius didesnis {num2}")
    