def calc_letter_frequencies(text):
    # Išfiltruojame ne abėcėlės simbolius ir konvertuojame viską į mažąsias raides, 
    # dėl vienodumo.
    return {i: text.lower().count(i) for i in text.lower() if i.isalpha()}


user_text = input("Įveskite tekstą: ")
letter_counts = calc_letter_frequencies(user_text)
print("Raidžių dažniai tekste:", letter_counts)