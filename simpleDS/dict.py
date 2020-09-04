from pprint import pprint

person = {
    "name": "Shukri",
    "Gender": "Male",
    "Occupation": "Researcher",
    "Home Planet": "Not sure yet"
    }

emptySet = {}
pprint(set())

pprint(type(emptySet))
# emptySet.add('something')

pprint(type(emptySet))

print(person)

print(person.pop("Gender"))
print(person["Occupation"])

person['Age'] = "26"

print(person)

word = {}
print(word)

word["key"] = "Value"
print(word)
