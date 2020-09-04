from task2.service.DataGenerator import DataGenerator
from task2.service.DataQuery import DataQuery


def main():
    print("Application is starting")
    print("Data Generator has been started")
    DataGenerator()
    print("Data Generation has been stopped")

    print("Data Query has been started")
    DataQuery()


if __name__ == '__main__':
    main()

