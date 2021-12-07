from binarytrees.binarytrees import BinaryTree,Node ,BinarySearch
from binarytrees.breadth import breadth_first




def test_breadth():
    tree = BinaryTree()
    tree.root=Node(1,Node(2,Node(3),Node(10)),Node(5,Node(6)))
    actual=[1, 2, 5, 3, 10, 6]
    expected=breadth_first(tree)
    assert expected == actual



def test_breadth_without_root():
    tree = BinaryTree()

    actual="there is no root "

    expected=breadth_first(tree)
    assert expected == actual
