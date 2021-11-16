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
    def __str__(self):
        """
        method to print and display the   values added
        """
        output = "top -> "
        if self.top is None:
            output += None
        else:
            current = self.top
            while(current):

                output += ("["+str(current.value)+"]"+" -> ")
                current = current.next
            output += "None"
            return output



if __name__ == '__main__':
    Pseudo_queue1=Stack()
    Pseudo_queue1.push(6)
    Pseudo_queue1.push(5)
    Pseudo_queue1.push(4)
    print(Pseudo_queue1)
