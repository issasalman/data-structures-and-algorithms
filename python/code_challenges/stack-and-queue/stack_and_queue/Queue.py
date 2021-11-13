from stack_and_queue.Node import Node


class Queue:
    """
    a class that implements the Queue Data structure
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        to add an item to the rear
        """
        node = Node(value)

        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        to remove an item from the front
        """

        if self.is_empty():
            raise Exception("The queue is empty")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        """
        to know the front
        """

        if self.is_empty():
            raise Exception("The queue is empty")

        return self.front.value

    def is_empty(self):
        """
        To check if the stack is empty or not
        """
        return self.front == None
