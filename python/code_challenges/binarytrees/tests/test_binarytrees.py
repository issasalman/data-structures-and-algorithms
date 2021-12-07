from binarytrees import __version__
from binarytrees.binarytrees import BinaryTree,Node ,BinarySearch




import pytest


def test_version():
    assert __version__ == '0.1.0'



def test_maximum_value():
        tree=BinaryTree()

        tree.root=Node(1,Node(2,Node(3),Node(10)),Node(5,Node(6)))
        excepted=10
        actual=tree.max_value()
        assert actual==excepted


def test_maximum_value_not_number():
     with pytest.raises(TypeError):
            tree=BinaryTree()
            tree.root=Node("A",Node("B"),Node("C"))
            tree.max_value()




def test_post_order_empty():
      with pytest.raises(Exception):
          tree=BinaryTree()
          tree.pre_order()




def test_root():
    tree=BinaryTree()
    tree.root=Node("A")
    assert tree.root.value == "A"

def test_leftchild_rightchild():
    tree=BinaryTree()
    tree.root=Node("A",Node("B"),Node("C"))
    assert tree.root.value == "A"
    assert tree.root.left.value == "B"
    assert tree.root.right.value == "C"




def test_pre_order(tree):

    excepted = ["A", "B", "D", "E", "C", "F"]
    assert tree.pre_order() == excepted

def test_in_order(tree):

    excepted = ['D', 'B', 'E', 'A', 'F', 'C']
    assert tree.in_order() == excepted

def test_post_order(tree):


    excepted = ['D', 'E', 'B', 'F', 'C', 'A']
    assert tree.post_order() == excepted

def test_add_to_root():
    bst = BinarySearch()
    bst.add(7)
    assert bst.root.value == 7
    assert bst.root.right == None


def test_add_multiple():
    bst = BinarySearch()
    values = [18, 8, 1, 14, 19, 30, 20, 16, 45]
    for value in values:
        bst.add(value)
    assert bst.root.value == 18

    assert bst.root.left.value == 8
    assert bst.root.left.left.value == 1
    assert bst.root.left.right.value == 14
    assert bst.root.right.value == 19
    assert bst.root.right.right.value == 30
    assert bst.root.right.right.left.value == 20
    assert bst.root.left.right.right.value == 16
    assert bst.root.right.right.right.value ==45




def test_contain():
    bst = BinarySearch()
    bst.add(7)
    assert bst.contains(7) == True
    assert bst.contains(5) == False



@pytest.fixture
def tree():

    tree=BinaryTree()
    tree.root=Node("A",Node("B",Node("D"),Node("E")),Node("C",Node("F")))
    return tree
