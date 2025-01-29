# Parašykite programą, kuri prašo vartotojo įvesti pradinę sumą, metinę palūkanų normą (procentais) ir laiką (metų skaičių).
# Apskaičiuokite paprastąsias palūkanas naudodami formulę PP=(P×N×L)/100 ir atspausdinkite rezultatą.

s = float(input("Suma: "))
l = float(input("Laikas: "))
p = float(input("Palūkanos: "))
pabrangimas = ((s * l * p) / 100)
print("Paprastos palūkanos: " , pabrangimas)