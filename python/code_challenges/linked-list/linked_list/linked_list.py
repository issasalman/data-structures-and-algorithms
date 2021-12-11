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
            return node

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
                    node.next = current.next.next
                    current.next.next = node
                    break
                current = current.next




    def deleteNode(self, key):
        current = self.head

        if self.head==None:
           return "empty list"
        elif self.head.value == key:

            self.head =self.head.next
            current=None
            return "Node Removed"
        while current.next:
            if current.next.value == key:
                if current.next.next:
                 temp=current.next
                 current.next=temp.next
                 temp=None
                else:
                    current.next=None

            if current.next:
                 current = current.next

    def deleteNodepos(self, position):

        if self.head == None:
            return

        current = self.head

        if position == 0:
            self.head =  current.next
            current = None
            return

        for i in range(position -1):
            current = current.next
            if current.next is None:
                break
        if current:
                 temp=current.next
                 current.next=temp.next
                 temp=None
        else:
            current.next=None



    def removeDuplicates(self):
        current = self.head
        if current == None:
            return
        while current.next:
            if current.value == current.next.value:
                temp=current.next
                new = temp.next
                current.next = new
                temp=None

            else:
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
        while current.next != None:
            current = current.next
            length += 1

        if k <0:
            return ("Please input positive numbers")

        if k > length:
            return ('k is greater than the length of the linked list')
        current = self.head

        for i in range(length - k ):
            current = current.next
        # print(current.value)
        return(current.value)

    def reverse_list(self):
         prev,current=None,self.head
         while current:
             following=current.next
             current.next=prev
             prev=current
             current=following
         self.head=prev


    def palindrom(self):
        fast=self.head
        current=self.head

        while fast and fast.next:
            fast=fast.next.next
            current=current.next
        prev=None
        while current:
             following=current.next
             current.next=prev
             prev=current
             current=following

        left,right=self.head,prev
        while right:
            if left.value!=right.value:
                return False

            left=left.next
            right=right.next
        return True

    def reorderlost(self) :
        fast=self.head.next
        current=self.head

        while fast and fast.next:
            fast=fast.next.next
            current=current.next
        prev=None
        while current:
             following=current.next
             current.next=prev
             prev=current
             current=following

        left,right=self.head,prev
        while left:
            tmp1,tmp2=left.next,right.next
            left.next=right
            right.next=tmp1
            left,right=tmp1,tmp2


    def deleteNodeNoHead(self, node):
         node.value= node.next.value
         node.next= node.next.next



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
            print("The slow list is empty")

            return (list1)
        while current1!=None and current2!=None:

            if current2:
                current = current1.next
                current1.next = current2
                current1 = current
            if current1:
                current = current2.next
                current2.next = current1
                current2 = current


if __name__ == '__main__':

    ll1 = LinkedList()
    # ll1.head=Node(1)
    # ll1.head.next=Node(2)

    # ll1.head.next.next=Node(3)


    ll1.append(21)
    ll1.append(4)
    ll1.append(4)
    ll1.append(1)
    ll1.append(8)




    ll1.append(4)
    ll1.append(21)




    # node=Node(15)

    # ll1.deleteNodeNoHead(node)

    # print(ll1.kthFromEnd(2))


    # print(ll1)
    # ll1.mergTwoList(ll1,ll2)
    # ll1.deleteNodepos(3)
    # ll1.reorderlost(ll1.head)
    print(ll1)

    print(ll1.deleteNodeNoHead(ll1.head))
    # ll2.append(5)
    # print(ll1.kthFromEnd(0))
    # print(zipLists(ll1,ll2))
    print(ll1)

