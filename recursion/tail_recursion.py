# linear recursion

def tail_recursion(n):
    if n > 0:
        print(n)
        tail_recursion(n - 1)


def tail_recursion_using_whileloop(n):
    while n > 0:
        print(n)
        n -= 1


print("Tail Recursion")
tail_recursion(4)

print("Tail Recursion using while loop")
tail_recursion_using_whileloop(4)
