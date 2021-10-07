def decrement(number):
    if number > 0:
        print(number)
        decrement(number - 1)
    else:
        return 0


if __name__ == "__main__":
    decrement(5)