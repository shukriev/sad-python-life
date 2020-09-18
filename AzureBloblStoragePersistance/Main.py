from persistance import Persist


def main():
    persist_decorator_test()


@Persist
def persist_decorator_test(): {
    print("Testing Persist")
}


if __name__ == '__main__':
    main()
