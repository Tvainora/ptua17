
# Parašykite Python programą, kuri apibrėžia du string kintamuosius, saugančius saugančias vartotojo vardą ir slaptažodį. Pradėkite begalinį ciklą, leidžiantį vartotojui įvesti vardą ir slaptažodį. 
# Jei duomenys yra teisingi, nutraukite begalinį ciklą ir atspausdinkite pasveikinimą.

vardas="pet321"
slaptazodis="pet123"

while True:
    input_vardas = input("Vartotojo vardas: ")
    input_slaptazodis = input("Vartotojo slaptazodis: ")
    if input_vardas == vardas and input_slaptazodis == slaptazodis:
        print(f"Sekmingai prisijunge! {vardas}")
        break
    elif input_vardas != vardas or input_slaptazodis != slaptazodis:
        print("Neteisingas slaptazodis arba vartotojo vardas")
    
    