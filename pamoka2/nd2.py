# Parašykite programą, kuri prašo vartotojo įvesti temperatūrą pagal Farenheitą, konvertuoja ją į Celsijaus laipsnius ir atspausdina rezultatą. 
#   Konvertavimo formulė yra C = (F−32) × 5/9​.

f = float(input("Temperatūra farengheitais: "))
c = (f - 32) * 5 / 9
print("Temperatūra celsijais: " , c)