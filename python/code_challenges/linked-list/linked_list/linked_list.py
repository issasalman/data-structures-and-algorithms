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

    def insert_before(self, val, valueAdded):
        node = Node(valueAdded)
        if self.head==None:
            self.head=node
        elif self.head.value == val:
            node.next = self.head
            self.head = node
        else:
            current = self.head

            while current.next !=None:

                if current.next.value == val:
                    node.next = current.next
                    current.next = node
                    break
                current = current.next


    def insert_after(self, val, valueAdded):

        """
        Method to add values after a specifc node
        """
        node = Node(valueAdded)

        if self.head==None:
            self.head=node

        elif self.head.value == val:
            node.next = self.head.next
            self.head.next = node
        else:
            current=self.head

            while current.next != None:

                if current.next.value == val:
                    current = current.next

                    node.next = current.next
                    current.next = node
                    break
                current = current.next



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

    def kthFromEnd(self, k):
        """
        This method is to return the value of a given index start counting the index from tail
        """
        current = self.head
        length = 0
        while current != None:
            current = current.next
            length += 1

        if k <0:
            print ("Please input positive numbers")
            return ("Please input positive numbers")

        if k > length:

            print('k is greater than the length of the linked list')
            return ('k is greater than the length of the linked list')
        current = self.head

        for i in range(length - k -1):
            current = current.next
        print(current.value)
        return(current.value)


def zipLists(list1,list2):
        current1 = list1.head
        current2 = list2.head
        if not current1 and not current2:
            print("The two lists are empty")
            return 'The two lists are empty'
        elif  not current1 :
            print("The first list is empty")

            return (list2)
        elif not current2:
            print("The second list is empty")

            return (list1)
        while current1!=None and current2!=None:


            if current2:
                temp = current1.next
                current1.next = current2
                current1 = temp
            if current1:
                temp = current2.next
                current2.next = current1
                current2 = temp


if __name__ == '__main__':

    ll1 = LinkedList()
    ll2 = LinkedList()

    ll1.append(5)
    ll1.append(5)

    ll2.append(5)

    zipLists(ll1,ll2)
    print(ll1)





