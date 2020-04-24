import sys

from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes
        # for us to call `insert` on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTreeNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)

        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)

        while q.len() > 0:
            node = q.dequeue()
            print(node.value)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.size > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
