from Queue import Queue

class karyNode:

    def __init__(self,value=None,children=[]):
        self.value = value
        self.children = children


class karyTree:
    def __init__(self,root=None):
        self.root = root



def fizz_buzz(number):

    if not number % 15:
        return "FizzBuzz"
    elif not  number%3 :
        return "Fizz"
    elif not number%5:
        return "Buzz"
    else:
        return str(number)

def fizz_buzz_tree(k_ary_tree ):

    if not k_ary_tree.root:
        return 'Tree is empty'

    queue = Queue()
    queue.enqueue(k_ary_tree.root)
    kary_tree = []

    while not queue.is_empty():
        front=queue.dequeue()
        front.value = fizz_buzz(front.value)
        for child in front.children:
            queue.enqueue(child)
        kary_tree.append(front.value)
    return kary_tree

if __name__ == '__main__':
    tree = karyTree()
    tree.root=karyNode(1,[karyNode(20,[karyNode(250),karyNode(35),karyNode(105)]),karyNode(3,[karyNode(333)]),karyNode(10,[karyNode(444)])])

    print(fizz_buzz_tree(tree))
