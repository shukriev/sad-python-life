import random

uniqueIntegerList = random.sample(range(1, 100), 10)

randomIntegerSubset = random.sample(uniqueIntegerList, 5)

print(uniqueIntegerList)

print(randomIntegerSubset)

try:
    with open('../task1/resource/output.txt', 'w') as file:
        file.write("%s\n" % place for place in randomIntegerSubset)
except FileNotFoundError as fnf_error:
    print(fnf_error)
