# Sukurkite programą, kuri prašo vartotojo atskirai įvesti savo vardą ir pavardę, o tada atspausdina juos oficialiai – 
# pirmiausia pavardė, po jos kablelis, tarpas, ir tada – vardas.

vardas = (input("Jūsų vardas: "))
pavarde = (input("Jūsų pavardė: "))
pakeistas = (f"{pavarde} , {vardas}")
print("Labas: " , pakeistas)