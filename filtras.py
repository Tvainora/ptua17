# VIDUTINIS

# Parašykite funkciją, kuri išfiltruoja ir surikiuoja restoranų sąrašą pagal jų reitingus. Kiekvienas restoranas turėtų būti reprezentuojamas kaip žodynas, kuriame yra raktai „name“ (pavadinimas) ir „rating“ (reitingas). Funkcija turėtų leisti vartotojui nurodyti minimalų reitingo slenkstį. Jei slenkstis nėra nurodytas, numatytoji reikšmė turėtų būti 4.0. Funkcija turėtų grąžinti abėcėlės tvarka surikiuotą restoranų pavadinimų sąrašą, kuriame būtų restoranai, atitinkantys arba viršijantys reitingo slenkstį.

# Funkcionalumas:

# Įvesties apdorojimas: Paprašykite vartotojo įvesti restoranų skaičių. Kiekvienam restoranui vartotojas turėtų pateikti pavadinimą ir reitingą.

# Reitingų filtravimas: Numatytoji reikšmė turi būti restoranai su 4.0 arba aukštesniu reitingu, nebent vartotojas nurodo kitą minimalų reitingą.

# Rikiavimas: Išvesties sąrašas su reitingo kriterijų atitinkančiais restoranas turėtų būti surikiuotas abėcėlės tvarka pagal restoranų pavadinimus.

# Bendravimas su vartotoju: Parodykite vartotojui surikiuotų restoranų, kurie atitinka reitingo kriterijus, sąrašą.


def rest_filtr (restourants, min_reiting):
    restourants_new = []

    rest_name = str(input("Name of the restourant: "))
    rest_reiting = float(input("Rating of the restourant"))
    restourants.append(restourants["name"])
    return sorted.restourants_new
