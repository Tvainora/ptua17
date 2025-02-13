def count_long_words(text):
    return len([word for word in text.split() if len(word) > 5])


user_text = input("Įveskite tekstą: ")
long_words_count = count_long_words(user_text)
print("Žodžių, ilgesnių nei penki simboliai, skaičius:", long_words_count)