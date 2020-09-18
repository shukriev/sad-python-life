from service.DataGenerator import DataGenerator
from service.DataQuery import DataQuery


def main():
    print("Application is starting")
    print("Data Generator has been started")
    DataGenerator()
    print("Data Generation has been stopped")

    print("Data Query has been started")
    DataQuery(file_name='./resource/task2.json')


if __name__ == '__main__':
    main()

