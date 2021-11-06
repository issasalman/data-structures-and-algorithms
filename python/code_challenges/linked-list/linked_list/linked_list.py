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

    def insert(self, valueAdded):
        node = Node(valueAdded)

        node.next = self.head

        self.head = node

        return "value added"

    @classmethod
    def countering(cls):
        return cls.counter

    def __str__(self):
        output = ""
        if self.head is None:
            output += None
        else:
            current = self.head
            while(current):

                output += ("{"+str(current.value)+"}"+" -> ")
                current = current.next
            output += "None"
            return output


    def search(self, valueSearched):
        current = self.head
        if self.head!=None:
            while current.next != None:
                if current.value == valueSearched:
                    print ("true")
                    return True

                current = current.next
            print ("false")
            return False
        else:
            print ("Empty")
            return ("Empty")


if __name__ == '__main__':

    ll = LinkedList()


    ll.insert(100)
    ll.insert('Issa')
    ll.insert(4)
    ll.append(5)

    print(ll)
    ll.search(100)



