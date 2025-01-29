
numbers = []

while True:
    
    entry = input("Įveskite skaičių (arba įveskite 'pabaiga'): ")
    if entry == "pabaiga":
        break

    numbers.append(float(entry))

if len(numbers) > 0:
    total = sum(numbers)
    average = total / len(numbers)
else:
    average = 0

print(f"Skaičiai: {numbers}")
print(f"Vidurkis: {average}")