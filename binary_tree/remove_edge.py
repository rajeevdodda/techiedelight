from binary_tree import BinaryTree

b_tree = BinaryTree()

for i in range(5):
    b_tree.push(i)


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def split_tree(root):
    return count_nodes(root) % 2 == 0


print(split_tree(b_tree.root))
b_tree.push(5)
print(split_tree(b_tree.root))
