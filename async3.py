import asyncio
import time


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    print(f"started at {time.strftime('%X')}")
    asyncio.run(main())
    print(f"finished at {time.strftime('%X')}")