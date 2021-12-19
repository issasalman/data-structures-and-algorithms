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



    def pre_order(self):
        """
        Traverse way called Depth First follows this order root >> left >> right
        """
        output = []
        if not self.root :
            raise Exception('Empty Tree')

        def traverse(root):
            output.append(root.value)
            if root.left :
                traverse(root.left)
            if root.right :
                traverse(root.right)

        traverse(self.root)
        return output


    def in_order(self):
        """
        Traverse way called Depth First follows this order left >> root >> right
        """
        output = []
        if not self.root :
            raise Exception('Empty Tree')

        def traverse(root):
            if root.left :
                traverse(root.left)
            output.append(root.value)

            if root.right :
                traverse(root.right)

        traverse(self.root)
        return output


    def post_order(self):
        """
        Traverse way called Depth First follows this order left >> right >> root
        """
        output = []
        if not self.root :
            raise Exception('Empty Tree')

        def traverse(root):
            if root.left :
                traverse(root.left)

            if root.right :
                traverse(root.right)

            output.append(root.value)


        traverse(self.root)
        return output

    def  max_value(self):
        """
        find maximum value in the tree

        """
        if not self.root :
            raise Exception('Empty Tree')

        self.maximum=0
        def traverse(node):
            if node.value >  self.maximum :
                self.maximum = node.value
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return  self.maximum




class BinarySearch(BinaryTree):
    """
    A class to build a sorted  binary tree that has maximum 2 children to make the searching faster
    """

    def add(self,value):
        """
        A method that Adds a new node with that value in the correct location in the binary search tree.
        """

        if not self.root:
            self.root = Node(value)

        else:
            def traverse(node):
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        traverse(node.left)

                else:
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        traverse(node.right)
            traverse(self.root)

    def contains(self, value):
        """
        A method that Returns: boolean indicating whether or not the value is in the tree at least once.
        """

        if not self.root:
            return False

        else:
            def traverse(node):
                if value == node.value:
                    return True

                if value > node.value:
                    if node.right:
                        return traverse(node.right)
                    else:
                        return False
                else:
                    if node.left:
                        return traverse(node.left)
                    else:
                        return False
            return traverse(self.root)

def amx_number(tree):
    root=tree.root
    if not root:
      return "empty tree"
    max_num=tree.root.value
    # max_last1=max_num
    # max_last2=max_num
    def traverse (node):
        nonlocal max_num
        # nonlocal max_last1
        # nonlocal max_last2

        if node.value>max_num:
           max_num=node.value

        if node.left:
           traverse(node.left)
        # if node.value>max_num:
        #    max_last1=node.value
        if node.right:
          traverse(node.right)


    traverse(root)
    return max_num

def create_tree():
    return tree

if __name__ == "__main__":
    tree=BinaryTree()
    tree.root=Node(1,Node(21,Node(3),Node(10)),Node(5,Node(6)))

    # print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())


    # tree1=BinarySearch()

    # print( tree1.add("a"))
    # print(tree1.contains('a'))
    print(amx_number(tree))


