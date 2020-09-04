vowels = {'h', 'i', 't', 'c', 'h', 's', 'i', 'k', 'e', 'r', 'a', 'h'}
word = input("Provide a word to search for vowels: ")
found = {""}

print(type(found))

print("Print Vowels First")
print(vowels)

print()

print("Print Found Second")
print(found)

print("------------------------------------")

for letter in word:
    if letter in vowels:
        found.add(letter)

print(found)
print("------------------------------------")

# for k in sorted(found):
#     print(k, "was found", found[k], "times.")

# print("------------------------------------")
# for k, v in found.items():
#     print(k, "was found", v, "times.")

# ------ Show boolean in not in ---------
print('h' in found)
print('z' in found)