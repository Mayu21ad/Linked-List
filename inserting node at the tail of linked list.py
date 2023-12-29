import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end=sep)
        node = node.next
        if node:
            print(sep, end='')

def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()
    for i in range(llist_count):
        llist_item = int(input())
        llist.head = insertNodeAtTail(llist.head, llist_item)
    print_singly_linked_list(llist.head, '\n')
