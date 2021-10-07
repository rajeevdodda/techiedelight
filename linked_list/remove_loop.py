# https://www.techiedelight.com/remove-loop-linked-list/

from linked_list import LinkedList

linked_list_instance = LinkedList()

for i in range(10):
    linked_list_instance.push(i)

linked_list_instance.display()


# setting loop
linked_list_instance.tail.next = linked_list_instance.head.next.next


def remove_loop_using_hash_map(node):
    prev = None
    hash_map = set()

    while True:
        if node in hash_map:
            prev.next = None
            break
        hash_map.add(node)
        prev = node
        node = node.next


temp = linked_list_instance.head

remove_loop_using_hash_map(temp)
print("\nAfter removing loop")
linked_list_instance.display()
