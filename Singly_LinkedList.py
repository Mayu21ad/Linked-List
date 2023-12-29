class SinglyLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

def printLinkedList(head):
    temp = head
    
    while temp is not None:
        print(temp.data)
        temp = temp.next

if __name__ == '__main__':
    llist_count = int(input("Enter the number of elements: "))
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input("Enter element: "))
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
