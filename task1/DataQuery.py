def find_missing_numbers(numbers: list):
    print(numbers)

    for n in range(100):
        if n not in numbers:
            print(n)


numberList = []

try:
    with open('../task2/resource/output.txt', 'r') as file:
        content = file.readlines()
except FileNotFoundError as fnf_error:
    print(fnf_error)
else:
    for line in content:
        number = line[:-1]
        numberList.append(int(number))
finally:
    print('Processing has been completed!')

find_missing_numbers(numberList)
