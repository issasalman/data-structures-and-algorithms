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



    def pre_order(self):
        """
        Traverse way called Depth First follows this order root >> left >> right
        """
        output = []
        if not self.root :
            raise Exception('Empty Tree')

        def traverse(root):
            if root :
                output.append(root.value)

                traverse(root.left)
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
             if root :

                traverse(root.left)
                output.append(root.value)

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
           if root :

                traverse(root.left)

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


        self.maximum=self.root.value
        def traverse(node):
            if node:

                if node.value >  self.maximum :
                    self.maximum = node.value
                traverse(node.left)
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
                    if  node.left:
                        traverse(node.left)

                    else:
                        node.left = Node(value)
                        return

                else:
                    if  node.right:
                        traverse(node.right)

                    else:
                        node.right = Node(value)
                        return

            traverse(self.root)
    def contains(self, value):
        """
        A method that Returns: boolean indicating whether or not the value is in the tree at least once.
        """

        def traverse(root):
            if root is None:
                return False
            if root.value == value:
                return True

            if root.value > value:
                return traverse(root.left)
            if root.value < value:
                return traverse(root.right)


        return traverse(self.root)


def max_number(tree):
    root=tree.root
    if not root:
      return "empty tree"
    max_num=tree.root.value
    def traverse (node):
        nonlocal max_num

        if node.value>max_num:
           max_num=node.value

        if node.left:
           traverse(node.left)
        if node.right:
          traverse(node.right)


    traverse(root)
    return max_num






def max_number1(tree):
    root=tree.root
    if not root:
      return "empty tree"
    max_num=tree.root.value
    sec=max_num
    counter=0
    def traverse (node):
        nonlocal max_num
        nonlocal counter
        nonlocal sec

        if node.right:
          traverse(node.right)


        if node.left:
           traverse(node.left)

        if node.value>max_num:
           max_num=node.value
           counter+=1


        if counter ==2:
               sec=node.value


    traverse(root)
    return sec




def min_number(tree):
    root=tree.root
    if not root:
      return "empty tree"

    min_num=tree.root.value
    sec=min_num
    def traverse (node):
        nonlocal min_num
        nonlocal sec



        if node.value<min_num:
           sec=min_num
           min_num=node.value

        if node.left:
           traverse(node.left)
        if node.right:
          traverse(node.right)


    traverse(root)
    return sec







def sum_of_nodes(tree):
    root=tree.root
    if not root:
      return "empty tree"
    sum_nodes=0
    def traverse (node):
        nonlocal sum_nodes

        if node:

            sum_nodes+=node.value


            traverse(node.left)

            traverse(node.right)


    traverse(root)
    return sum_nodes


def sum_of_leaves(tree):
    root=tree.root
    if not root:
      return "empty tree"
    sum_nodes=0
    def traverse (node):
        nonlocal sum_nodes
        if node:

           if node.left==None and node.right==None:
                sum_nodes+=node.value


           traverse(node.left)

           traverse(node.right)


    traverse(root)
    return sum_nodes

def num_of_leaves(tree):
    root=tree.root
    if not root:
      return "empty tree"
    sum_nodes=0
    def traverse (node):
        nonlocal sum_nodes


        if node.left==None and node.right==None:
             sum_nodes+=1

        if node.left:
           traverse(node.left)
        if node.right:
          traverse(node.right)


    traverse(root)
    return sum_nodes


def univalue(tree):
    queue=Queue()
    x=tree.root

    if  tree.root:
            queue.enqueue(tree.root)
    else:
        return "there is no root "

    flag=True

    while not queue.is_empty():
        front=queue.dequeue()
        if x.value!=front.value:
            flag=False


        if front.left :
                queue.enqueue(front.left)
        if front.right :
                queue.enqueue(front.right)
    return flag



def mergeinone(root1,root2):
        if (not root1):
           return root2

        if (not root2):
           return root1
        root1.value+=root2.value
        root1.left=mergeinone(root1.left,root2.left)
        root1.right=mergeinone(root1.right,root2.right)
        return root1



    #        5
    #     3     8
    #    1 4  7   12
    #           10
    #          9  11


def find_largest( root):
        current = root
        while current:
            if not current.right:
                 return current.value
            current= current.right
def find_second_largest( root):
        if (root is None or root.left is None and root.right is None):
            return "empty"
        current = root
        while current:
             if not current.right and  current.left :
                 return find_largest(current.left)
             if (current.right and not current.right.left and not current.right.right):
                 return current.value
             current = current.right


def find_min( root):
        current = root
        while current:
            if not current.left:
                 return current.value
            current= current.left

def find_second_min( root):
        if (root is None or root.left is None and root.right is None):
            return "empty"
        current = root
        while current:
             if not current.left and  current.right :
                 return find_min(current.right)
             if (current.left and not current.left.left and not current.left.right):
                 return current.value
             current = current.left



if __name__ == "__main__":
    tree=BinaryTree()
    tree.root=Node(4,Node(2),Node(3,Node(1)))
    tree1=BinaryTree()
    tree1.root=Node(8,Node(21,Node(3),Node(5)),Node(8,Node(6,Node(5)),Node(81)))

    # print(univalue(tree))
    # print(tree.max_value())
    # print(tree.pre_order())

    # tree2=BinarySearch()

    # print( tree2.add(4))
    # print( tree2.add(1))
    # print( tree2.add(2))


    # print( tree2.add(5))
    # print( tree2.add(6))

    # print( tree2.add(4))
    # print( tree2.add(5))
    # print( tree2.add(3))
    # print( tree2.add(8))
    # # print(tree2.pre_order())



    # # print(tree2.contains(6))
    # print(find_second_largest(tree2.root))
    # print(find_second_min(tree1.root))
    print(min_number(tree1.root))
    # print(sum_of_nodes(tree))
    # print(sum_of_leaves(tree))
    # print(num_of_leaves(tree))










