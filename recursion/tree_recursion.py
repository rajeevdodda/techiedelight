def tree_recursion(n):
    if n > 0:
        print(n)
        tree_recursion(n - 1)
        tree_recursion(n - 1)


print(tree_recursion(3))
