class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x
