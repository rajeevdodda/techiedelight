def function_a(n):
    if n > 0:
        print(n)
        function_b(n - 1)


def function_b(n):
    if n > 1:
        print(n)
        function_a(n // 2)


function_b(10)
