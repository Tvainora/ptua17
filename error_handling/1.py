# try:
#     print("I am here!")
#     print(2 / 0)
# except Exception as e:
#     print(f"Learn some basic math dude!,because off error: {e}")


# try:
#     # print("I am here!")
#     print(2 / 0)
# except ZeroDivisionError:
#     print(f"CAN'T DIVIDE BY ZERO!")


# try:
#     input = int(input("Enter a number: "))
#     print(input)
# c


# def print_message(message:str) -> str:
#   try:
#     # doing something with message and so on
#     return message
#   except Exception as e:
#     # printig or logging error




# Python’e dalyba iš nulio iššaukia ZeroDivisionError. Jūsų užduotis – sukurti funkciją (), kuri:

# Priima du skaičius kaip argumentus.

# Bando padalinti pirmąjį skaičių iš antrojo.

# Jei antrasis skaičius yra 0, ji turi sugauti ZeroDivisionError ir grąžinti jūsų užrašytą klaidos pranešimą.

# Jei bent vienas iš įvestų argumentų nėra skaičius, ji turi pagauti TypeError ir grąžinti jūsų užrašytą klaidos pranešimą.

# Jei neįvyko jokių išimčių, ji turėtų išspausdinti pranešimą Dalyba buvo sėkminga (naudojant else bloką).

# Nepaisant to, ar dalyba pavyko, ar ne, ji turėtų išspausdinti pranešimą Buvo bandyta atlikti dalybą.

# Jei dalyba pavyko, ji turėtų grąžinti rezultatą (arba else bloke, arba funkcijos pabaigoje).


import logging

logging.basicConfig(
    level=logging.ERROR,
    filename="ups.txt",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",)

def safe_divide(a, b):
    try:
        c = a / b
    except Exception as e:
        logging.error(f"Error! {e}")
        return "Devision by zero is imposible!"
    except Exception as e:
        logging.error(f"Error! {e}")
        return "Number not found! Please enter a number!"
    else:
        print("Sucess! Division was possible!")
        return c


print(safe_divide(10, 0))
print(safe_divide(10, "hello world"))
print(safe_divide(10, 2))
