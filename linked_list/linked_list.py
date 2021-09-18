class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        self.tail = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        node = Node(element)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next, self.tail = node, node

    def remove_head(self):
        if self.head:
            head = self.head.data
            self.head = self.head.next
            return head
        else:
            return None


if __name__ == "__main__":
    linked_list = LinkedList()

    for i in range(10):
        linked_list.push(i)

    node = linked_list.head

    while node:
        print(node.data, end=" -> ")
        node = node.next
