"""
.venv/bin/python run_directly.py \
    example/callable_class_instance/sync_instance.py \
    --output example/callable_class_instance/sync_instance.png \
    --language py
    
.venv/bin/python -m debugpy --listen localhost:5678 --wait-for-client run_directly.py \
    example/callable_class_instance/sync_instance.py \
    --output example/callable_class_instance/sync_instance.png \
    --language py

"""

import asyncio


class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x


class AsyncAdder:
    def __init__(self, value):
        self.value = value

    async def __call__(self, x):
        return self.value + x


def main():
    add_five = Adder(5)
    result1 = add_five(10)
    print(result1)


async def async_main():
    async_add_five = AsyncAdder(5)
    result2 = await async_add_five(11)
    print(result2)


if __name__ == "__main__":
    main()
    asyncio.run(async_main())
