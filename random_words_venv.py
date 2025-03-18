from random_word import RandomWords

# Create an instance of RandomWords
r = RandomWords()

# Generate 5 random words
random_words = [r.get_random_word() for _ in range(5)]

# Convert each word to uppercase
uppercase_words = [word.upper() for word in random_words]

# Sort the words alphabetically
sorted_words = sorted(uppercase_words)

for word in sorted_words:
    print(word)