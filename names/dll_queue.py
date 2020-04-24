import sys

from doubly_linked_list import DoublyLinkedList

"""
Should have the methods: enqueue, dequeue, and len.
    - `enqueue` should add an item to the back of the queue.
    - `dequeue` should remove and return an item from the front of the queue.
    - `len` returns the number of items in the queue.
"""


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        """ Answer: Because it's linear data structure lends itself well to a list of items like a que.
        Ques and DLL go together like peas in a pod. """
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
