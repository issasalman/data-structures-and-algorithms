from binarytrees.Queue import Queue

class karyNode:

    def __init__(self,value=None,children=[]):
        self.value = value
        self.children = children

class karyTree:
    def __init__(self,root=None):
        self.root = root


def fizz_buzz(number):

    if  number % 15==0:
        return "FizzBuzz"

    elif   number%3 ==0:
        return "Fizz"

    elif  number%5==0:
        return "Buzz"

    else:
        return str(number)

def fizz_buzz_tree(k_ary_tree ):
    queue = Queue()
    kary_tree = []

    if  k_ary_tree.root:
            queue.enqueue(k_ary_tree.root)
    else:
        return "empty tree"

    while not queue.is_empty():
        front=queue.dequeue()
        front.value = fizz_buzz(front.value)
        for child in front.children:
            queue.enqueue(child)
        kary_tree.append(front.value)
    return kary_tree

# if __name__ == '__main__':
#     tree = karyTree()
#     tree.root=karyNode(1,[karyNode(20,[karyNode(250),karyNode(35),karyNode(105)]),karyNode(3,[karyNode(333)]),karyNode(10,[karyNode(444)])])

#     print(fizz_buzz_tree(tree))
