class Node:

    """
    Function to initialise the node Class
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Creating Nodes in linked List way
    """
    counter=0
    def __init__(self):
        self.head = None


    def append(self, valueAdded):

        node = Node(valueAdded)
        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.next != None:
                current = current.next

            LinkedList.counter += 1
            current.next = node
            return "value added"


    @classmethod
    def countering(cls):
        return cls.counter

    def __str__(self):
        output = "head -> "
        if self.head is None:
            output += None
        else:
            current = self.head
            while(current):
                output += f"{current.value} -> "
                current = current.next
            output += "None"
            return output
    def search(self, valueSearched):


        current = self.head


        while current != None:
            if current.value == valueSearched:
                print ("true")
                return True

            current = current.next
        print ("false")
        return False


if __name__ == '__main__':

    ll = LinkedList()


    ll.append(100)
    ll.append('Issa')
    ll.append(4)
    print(ll)
    ll.search(4)



