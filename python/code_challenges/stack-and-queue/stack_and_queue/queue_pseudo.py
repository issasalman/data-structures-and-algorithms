
from stack_and_queue.Stack import Stack

class Pseudo_queue:
    """
    a class that implements the Stack Data structure
    """

    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()


    def enqueue(self,value):
        """
        to add an item to the rear
        """
        self.stack1.push(value)
        return value


    def dequeue(self):

        """
         to remove the  item that was first added
        """
        if not self.stack1.top:
            raise Exception("empty")

        while self.stack1.top:
            temp1=  self.stack1.pop()
            self.stack2.push(temp1)
        temp2=self.stack2.pop()


        while self.stack2.top:
            temp1=  self.stack2.pop()
            self.stack1.push(temp1)
        return temp2

    def __str__(self):
        return  self.stack1.__str__()


if __name__ == '__main__':
    Pseudo_queue1=Pseudo_queue()
    Pseudo_queue1.enqueue(6)
    Pseudo_queue1.enqueue(5)
    Pseudo_queue1.enqueue(4)

    print(Pseudo_queue1)














