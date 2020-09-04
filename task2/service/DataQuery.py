import json


class DataQuery(object):

    def __init__(self):
        print("Data Query Analyzing for missing persons")

        try:
            with open('./resource/task2.json', 'r') as person_stream:
                persons = json.loads(person_stream.read())
                self.find_missing_persons(persons)
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        finally:
            person_stream.close()

    @staticmethod
    def find_missing_persons(input_list: list):
        """Find missing persons from given all_person.json file"""
        try:
            with open('./resource/all_person.json', 'r') as all_person_stream:
                all_persons = json.loads(all_person_stream.read())

                for single_person in all_persons:
                    print(single_person)

        except FileNotFoundError as fnf_err:
            print(fnf_err)
        finally:
            all_person_stream.close()
