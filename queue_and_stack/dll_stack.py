import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # Use DLL's add to head function
        # It will take care of whether or not it's an empty DLL
        pass

    def pop(self):
        # Use DDL's remove from head function
        # It will take care of whether or not it's an empty DLL
        pass

    def len(self):
        # Return the length of the DLL
        pass
