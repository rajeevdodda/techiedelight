def add(n: int):
    if n == 0:
        return 0
    return add(n - 1) + n


print(add(4))
