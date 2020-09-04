vowels = ['h', 'i', 't', 'c', 'h', 's', 'i', 'k', 'e', 'r', 'a', 'h']
word = input("Provide a word to search for vowels: ")
found = {}

print("Print Vowels First")
print(vowels)

print()

print("Print Found Second")
print(found)
print("------------------------------------")

for letter in word:
    if letter in vowels:
        if letter in found:
            found[letter] += 1
        else:
            found[letter] = 1
        #     ----------------------------
        #     Option 2 by using setdefault
        # if letter in found:
        #     found.setdefault(letter, 0)
        #     found[letter] += 1

print(found)
print("------------------------------------")

for k in sorted(found):
    print(k, "was found", found[k], "times.")

print("------------------------------------")
for k, v in found.items():
    print(k, "was found", v, "times.")

print('h' in found)
print('z' in found)
