# You have a list of ten random words which starts with letters A, C, or P.
# Write a function that takes a list of the word_list and prints new list 
# with all words that starts with letter P.

# names_list = ["Antanas", "Petras", "Jonas", "Paulius", "Cezaris", "Andrius", "Pavelas", "Celsius", "Petronele", "Pasatas"]
# names_list.sort()
# print(names_list)





word_list = ['Apple', 'Car', 'Proud', 'Apricot', 'Plank', 'Calk', 'Alphabet', 'Cork', 'August', 'Plain', 'peach']

def starts_with_p(word_list: List[str]) -> List[str]:
    p_words: List[str] = []
    for word in word_list:
        if word.upper().startswith('P'):
            p_words.append(word)
    return p_words
print(starts_with_p(word_list))



def extract_specific_words(word_list: List[str]) -> List[str]:
    return [name for name in word_list if name.upper().startswith('P')]
