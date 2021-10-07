# linear recursion

def head_recursion(n):
    if n > 0:
        head_recursion(n - 1)
        print(n)


def head_recursion_using_while_loop(n):
    i = 1
    while i <= n:
        print(i)
        i += 1


print("Head Recursion")
head_recursion(4)

print("Head recursion using while loop")
head_recursion_using_while_loop(4)