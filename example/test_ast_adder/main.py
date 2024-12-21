from adder import Adder


def main():
    add_five = Adder(5)
    result = add_five(10)
    print(result)

if __name__ == "__main__":
    main()