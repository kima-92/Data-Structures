import sys
sys.path.append('../doubly_linked_list')
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Check if new value is less than self.value
        if value < self.value:
            # Check if there is a value in self.left

            # If there is no value in self.left
            if not self.left:
                # Create a new BinarySearchTree node with this new value
                # Set it to be tis node's left child (node)
                self.left = BSTNode(value)
            # Else: If there IS a self.left
            else:
                # Use recursion (call the current function again) to attempt
                # the same thing on the BinarySearchTree child node to the left
                self.left.insert(value)
        # Else, if new value is grater than self.value
        else:
            # If there is no value in self.right
            if not self.right:
                # Create a new BinarySearchTree node with this new value
                # Set it to be tis node's right child (node)
                self.right = BSTNode(value)
            # If there IS a self.right
            else:
                # Use recursion (call the current function again) to attempt
                # the same thing on the BinarySearchTree child node to the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if self.value is the target
        if self.value == target:
            # Return true
            return True
        
        # If the target is lower than self.value
        if target < self.value:
            # If there's nothing at self.left
            if not self.left:
                # Return false
                return False
            # Else: If there is something in self.left
            else:
                # Use recursion. Call this method again to 
                # perform the same steps to self.left
                return self.left.contains(target)     # This fucntion returns a bool
        # Else: If target is greater than self.value
        else:
            # If there is nothing in self.right
            if not self.right:
                # Return false
                return False
            # Else: If there is something in self.right
            else:
                # Use Recursion. Call this function again to 
                # try and find the target at self.right
                return self.right.contains(target)    # This function returns a bool

    # Return the maximum value found in the tree
    def get_max(self):
        # If there is nothing in self.right
        if not self.right:
            # Return self.value
            return self.value
        # Else: If there is something in self.right
        else:
            # Use recursion. Call this function again to
            # perform the same steps on self.right
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Use this fn function on self.value
        fn(self.value)

        # If self.left is not empty
        if self.left:
            # Use recursion to call use fn in self.left
            self.left.for_each(fn)
        # If self.right is not empty
        if self.right:
            # Use recursion to call this same function on self.right
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Check if this node is not empty
        if node:
            # Call this same function on the node to the left ( smaller )
            self.in_order_print(node.left)
            # When it comes back from this recursion, 
            # print the current value
            print(node.value)
            # Attempt recursion on the right node ( greater )
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Check if this node is not empty
        if node:
            # Create a queue
            my_queue = Queue()
            # enqueue node
            my_queue.enqueue(node)

            # While the length of my_queue is not 0
            while my_queue.len() != 0:
                # save the last node in the queue in popped_node
                # dequeue this last node from the queue
                dequeued_node = my_queue.dequeue()
                # print the value of popped_node 
                print(dequeued_node.value)

                # If popped_node.left is not empty
                if dequeued_node.left:
                    # Enqueue popped_node.left to the queue
                    my_queue.enqueue(dequeued_node.left)
                
                # If popped_node.right is not empty
                if dequeued_node.right:
                    # Enqueue popped_node.right to the queue
                    my_queue.enqueue(dequeued_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # If there is a node
        if node:
            # Save the current node in current
            current = node
            # Create a stack
            my_stack = Stack()

            # While (current is not None) or (my_stack.len is not 0)
            while current or my_stack.len() != 0:
                # if current is not empty
                if current:
                    # Add current to the stack ( push )
                    my_stack.push(current)
                    # print the value of current
                    print(current.value)
                    # Make current.left the new current node
                    # So we can keep going left
                    current = current.left
                # Else: If current is empty
                else: 
                    # pop from the stack the last node added
                    # Save that node in popped_node
                    popped_node = my_stack.pop()
                    # Save popped_node.right as current
                    # So we can check if popped_node.right is 
                    # empty in the next while loop
                    current = popped_node.right

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass