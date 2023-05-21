import time


def count():
    print("One")
    time.sleep(1)
    print("Two")


def main():
    for _ in range(3):
        count()


if __name__ == "__main__":
    print(f"started at {time.strftime('%X')}")
    main()
    print(f"finished at {time.strftime('%X')}")