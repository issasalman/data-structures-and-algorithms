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


    def in_order(self):
        """
        Traverse way called Depth First follows this order left >> root >> right
        """
        output = []
        if not self.root :
          return None

        def traverse(root):
            if root.left :
                traverse(root.left)
            output.append(root.value)

            if root.right :
                traverse(root.right)

        traverse(self.root)
        return output

