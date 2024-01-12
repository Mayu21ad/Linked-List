class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def insertNodeAtPosition(llist, data, position):
    node = SinglyLinkedListNode(data)

    if llist.head is None:
        llist.head = node
    else:
        temp = llist.head

        count = 1
        while temp.next is not None and count < position:
            temp = temp.next
            count += 1

        node.next = temp.next
        temp.next = node

    return llist

linked_list = SinglyLinkedList()

linked_list = insertNodeAtPosition(linked_list, 1, 1)
linked_list = insertNodeAtPosition(linked_list, 2, 2)
linked_list = insertNodeAtPosition(linked_list, 3, 2)

current_node = linked_list.head
while current_node is not None:
    print(current_node.data, end=" ")
    current_node = current_node.next
