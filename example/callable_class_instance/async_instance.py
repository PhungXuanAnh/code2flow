"""
.venv/bin/python run_directly.py \
    example/callable_class_instance/async_instance.py \
    --output example/callable_class_instance/async_instance.png \
    --language py
    
.venv/bin/python -m debugpy --listen localhost:5678 --wait-for-client run_directly.py \
    example/callable_class_instance/async_instance.py \
    --output example/callable_class_instance/async_instance.png \
    --language py

"""

import asyncio


class AsyncAdder:
    def __init__(self, value):
        self.value = value

    async def __call__(self, x):
        return self.value + x


async def main():
    add_five = AsyncAdder(5)
    result2 = await add_five(11)
    print(result2)


if __name__ == "__main__":
    asyncio.run(main())
