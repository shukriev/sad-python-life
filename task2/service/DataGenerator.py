import json
import random
import itertools

from task2.config.Config import Config
from task2.model.Person import Person, PersonEncoder


class DataGenerator(object):
    _first = Config.get_configuration('first-name')
    _last = Config.get_configuration('last-name')

    def __init__(self):
        try:
            with open('./resource/task2.json', 'w') as fl:
                fl.write(json.dumps(random.sample(self.generate_random_persons(), 20), indent=4, cls=PersonEncoder))
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        except TypeError as te_error:
            print(te_error)
        finally:
            fl.close()

    def generate_random_persons(self) -> list:
        """Generate random persons by given names from configuration file"""
        persons = list()

        for person in itertools.product(self._first, self._last):
            persons.append(Person(person[0], person[1], int(random.choice(range(1, 70)))))

        try:
            with open('./resource/all_person.json', 'w') as f:
                f.write(json.dumps(persons, indent=4, cls=PersonEncoder))
        except FileNotFoundError as e:
            print(e)
        finally:
            f.close()

        return persons

