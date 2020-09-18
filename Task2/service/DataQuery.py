import json
import os
import typing

if typing:
    from typing import List


class DataQuery(object):

    def __init__(self, file_name: str):

        assert os.path.isfile(file_name), "Invalid file!"

        print("Data Query Analyzing for missing persons")
        self.file_name = file_name

        try:
            with open(self.file_name, 'r') as all_person_stream:
                persons = json.loads(all_person_stream.read())
                self.find_missing_persons(persons)

                all_person_stream.close()
        except FileNotFoundError as fnf_error:
            print(fnf_error)

    @staticmethod
    def find_missing_persons(input_list: List[str]):
        """Find missing persons from given all_person.json file"""
        try:
            with open('./resource/all_person.json', 'r') as all_person_stream:
                all_persons = json.loads(all_person_stream.read())

                # PRINT ALL PERSONS
                # for single_person in all_persons:
                #     print(single_person)

        except FileNotFoundError as fnf_err:
            print(fnf_err)
        finally:
            all_person_stream.close()
