vowels = ['h', 'i', 'i', 't', 'c', 'h', 'h', 'i', 'k', 'e', 'r']
word = input("Provide a word to search for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)
