"""
.venv/bin/python run_directly.py \
    example/callable_class_instance/callable_class_instance.py \
    --output example/callable_class_instance/result.png \
    --language py
"""
class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x


def main():
    # Create an instance of the Adder class
    add_five = Adder(5)

    # Call the instance as if it were a function
    result = add_five(10)

    # Print the result
    print(result)


if __name__ == "__main__":
    main()
