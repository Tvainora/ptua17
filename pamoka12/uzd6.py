def is_square(num):
    root = math.sqrt(num)  # arba root = num ** 0.5
    return root == int(root)


num = int(input("Įveskite sveikąjį skaičių: "))
result = is_square(num)
print(f"Ar {num} yra kito skaičiaus kvadratas? {'Tiesa' if result else 'Netiesa'}")