from Queue import Queue
class Node:
    """
    A class to initialise a node with a properties like value ,left and right for a tree
    """
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left=left
        self.right=right



class BinaryTree:
    """
    A class to build a binary tree that has maximum 2 children
    """
    def __init__(self,root=None):
        self.root = root



def breadth_first(tree):
    """
    A function to traverse the tree row by row
    """
    queue=Queue()
    final_output = []

    if  tree.root:
            queue.enqueue(tree.root)
    else:
        return "there is no root "

    while not queue.is_empty():
        front=queue.dequeue()
        final_output.append(front.value)

        if front.left :
                queue.enqueue(front.left)
        if front.right :
                queue.enqueue(front.right)
    return final_output

tree = BinaryTree()
tree.root=Node(1,Node(2,Node(3),Node(10)),Node(5,Node(6)))
actual=[1, 2, 5, 3, 10, 6]
print(breadth_first(tree))
