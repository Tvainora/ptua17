# Parašykite programą, kuri paima vartotojo vardą iš jo įvesto pilno vardo ir sukuria asmeninį pasveikinimą. Pilnas vardas įvedamas formatu „Vardas Pavardė“. 
# Pasveikinime vardas turi būti užrašytas visomis didžiosiomis raidėmis.


full_name = input("Koks vardas??: ")
space_index = full_name.find(" ")
first_name = full_name[:space_index]
first_name_upper = first_name.upper()
greeting = f"Labas, {first_name.upper()}, tau ragas!"
print(greeting)