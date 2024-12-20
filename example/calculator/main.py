"""
.venv/bin/python run_directly.py \
    example/calculator \
    --output example/calculator/result.png \
    --language py
"""

from calculator import Calculator


def main():
    calc = Calculator()
    x = 10
    y = 5

    sum_result = calc.add(x, y)
    print(f"Sum: {sum_result}")

    diff_result = calc.subtract(x, y)
    print(f"Difference: {diff_result}")

    prod_result = calc.multiply(x, y)
    print(f"Product: {prod_result}")

    div_result = calc.divide(x, y)
    print(f"Quotient: {div_result}")


if __name__ == "__main__":
    main()
