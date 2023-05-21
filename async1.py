"""

coroutine - function with async & await keywords

We use `await` keyword to simply suspend current execution and execute another
coroutine



"""


import asyncio


async def main():   # `main` is name of coroutine
    print("hello")
    await asyncio.sleep(1)  # `await` keyword suspends execution in the middle.
    print("world")


asyncio.run(main())

# `asyncio.run()` tells python that this coroutine needs to be executed in
# `async` environment


