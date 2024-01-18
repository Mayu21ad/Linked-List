class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode(llist, position):
    if position == 0:
        llist = llist.next
    else:
        temp = llist
        count = 1
        while temp.next is not None and count < position:
            temp = temp.next
            count += 1
        if temp.next is not None:
            temp.next = temp.next.next
        else:
            print("Position out of bounds.")

    return llist
