from stack_and_queue.Node import Node


class Stack:
    """
    a class that implements the Stack Data structure
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """
         to add an item to the top of stack
        """
        node = Node(value)
        if self.top:
            node.next = self.top

        self.top = node

    def pop(self):
        """
         to remove an item from the top
        """

        if self.is_empty():
            raise Exception("This stack is empty")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value


    def peek(self):

        """
         to know the top value
        """
        if self.is_empty():
            raise Exception("This stack is empty")
        return self.top.value

    def is_empty(self):
        """
        To check if the stack is empty or not
        """
        return self.top == None
