from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    @staticmethod
    def preorder(root):
        if root is None:
            return
        print(root.data, end=' ')
        BinaryTree.preorder(root.left)
        BinaryTree.preorder(root.right)

    def push(self, element):
        print(element)
        if self.root is None:
            self.root = Node(element)
            return
        else:
            q = deque()
            q.append(self.root)

            while len(q):
                node = q.popleft()
                # print(node.data)

                if node.left is None:
                    node.left = Node(element)
                    break
                else:
                    q.append(node.left)

                if node.right is None:
                    node.right = Node(element)
                    break
                else:
                    q.append(node.right)
