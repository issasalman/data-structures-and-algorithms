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
    def insert_before(self,val,valueAdded):
        """
        Method to add values before a specifc node
        """
        node=Node(valueAdded)
        if self.head == None:
            self.head = node
        else:
            current=self.head

        while current.next != None:
            if current.value == val:
                node.next=self.head
                self.head=node
                break
            if current.next.value == val:
                node.next = current.next
                current.next = node
                break

            else:
                current = current.next


    def insert_after(self, val, valueAdded):

        """
        Method to add values after a specifc node
        """
        node=Node(valueAdded)


        if self.head is None:
            self.head = node
        else:
            current=self.head

            while current.next != None:
                current = current.next

                if current.value == val:
                    node.next = current.next
                    current.next = node
                    break



    def insert(self, valueAdded):
        """
        Method to add values at the beginning  nodes
        """
        node = Node(valueAdded)

        if self.head:

            LinkedList.counter += 1

            node.next = self.head

            self.head = node
        else:

            self.head = node

        return "value added"

    @classmethod
    def countering(cls):
        """
        method to count the number of values added
        """
        return cls.counter

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

                output += ("["+str(current.value)+"]"+" -> ")
                current = current.next
            output += "None"
            return output


    def includes(self, valueSearched):
        """
        method to search for a specifc value
        """
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


    ll.append(5)
    ll.append(4)
    ll.append(3)

    ll.append(52)


    ll.insert_after(52,30)
    print(ll)
    ll.includes(100)



