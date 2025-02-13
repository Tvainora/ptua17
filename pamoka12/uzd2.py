# Įveskite tekstą: Šioje paskaitoje aptarsime papildomas Python integruotų duomenų struktūrų funkcijas.
# Žodžių su 'e' skaičius: 5


# user_text = input("Įveskite tekstą: ")
# words_with_e = count_words_with_e(user_text)
# print("Žodžių su 'e' skaičius:", words_with_e)

text =str(input("Enter your text here: "))
letter = 'e'
count = sum(1 for word in text if letter in word)
print(count)