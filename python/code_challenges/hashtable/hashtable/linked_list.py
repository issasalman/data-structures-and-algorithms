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
        """
        Method to add values to the end of nodes
        """
        LinkedList.counter += 1


        node = Node(valueAdded)

        if self.head == None:
            self.head = node

        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = node
            return "value added"




    def insert(self, valueAdded):
        """
        Method to add values at the beginning  nodes
        """
        node = Node(valueAdded)

        if self.head==None:
            self.head=node

        else:

            node.next=self.head

            self.head=node


        return "value added"



    def __str__(self):
        """
        method to print and display the   values added
        """
        output = "head -> "
        if self.head is None:
            output += None
        else:
            current = self.head
            while(current):

                output += (str(current.value)+" -> ")
                current = current.next
            output += "None"
            return output

if __name__ == '__main__':

    ll1 = LinkedList()

    ll1.append(5)
    ll1.append(8)
    ll1.append(2)


    print(ll1)
