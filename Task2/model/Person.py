from json import JSONEncoder


class Person:
    def __init__(self, first_name, last_name, age):
        if not isinstance(age, int):
            raise TypeError("age must be an integer")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return '{} {} - {} years old'.format(self.first_name, self.last_name, self.age)


class PersonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

