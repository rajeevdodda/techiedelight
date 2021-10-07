def nested_recursion(n):
    if n > 100:
        return n - 10
    else:
        return nested_recursion(nested_recursion(n+11))


print(nested_recursion(95))