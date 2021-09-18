# https://www.techiedelight.com/construct-complete-binary-tree-from-linked-list/

from linked_list.linked_list import LinkedList
from binary_tree import BinaryTree

linked_list_instance = LinkedList()
binary_tree_instance = BinaryTree()

for i in range(4):
    linked_list_instance.push(i)


def convert_ll_to_bt(linked_list: LinkedList):
    node = linked_list.head

    while node:
        binary_tree_instance.push(node.data)
        node = node.next


convert_ll_to_bt(linked_list_instance)

binary_tree_instance.preorder(binary_tree_instance.root)
