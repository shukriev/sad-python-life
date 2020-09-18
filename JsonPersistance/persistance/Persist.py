class Persist:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # We can add some code
        # before function call

        self.function(*args, **kwargs)

        print("JSON PERSISTANCE")
        # We can also add some code
        # after function call.
