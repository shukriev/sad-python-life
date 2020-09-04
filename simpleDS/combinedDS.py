import pprint

person = {
    "Name": "The REAL name",
    "Gender": "Mixed"
}

print(person)

person["PersonLink"] = person

print(person)

mixedGender = ["Male", "Female"]

person["MixedGender"] = mixedGender

print(person)

# Sexy Print

pprint.pprint(person)
