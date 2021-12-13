from hashtable.binary_tree import BinaryTree, Node

from hashtable.tree_intersection import tree_intersection


def test_tree_intersection():
    tree1 = BinaryTree()
    tree1.root=Node(1,Node(4,Node(3),Node(55)),Node(2,Node(3)))

    tree2 = BinaryTree()
    tree2.root=Node(4,Node(4,Node(3),Node(55)),Node(2,Node(32)))


    actual = tree_intersection(tree1, tree2)
    expected = [3, 4, 55, 4, 2]
    assert actual == expected


def test_tree_intersection_trees_empty():
    tree1 = BinaryTree()

    tree2 = BinaryTree()


    actual = tree_intersection(tree1, tree2)
    expected = []
    assert actual == expected

def test_tree_no_intersection():
    tree1 = BinaryTree()
    tree1.root=Node(1,Node(4,Node(3),Node(55)),Node(2,Node(3)))

    tree2 = BinaryTree()
    tree2.root=Node(42,Node(34,Node(33),Node(554)),Node(25,Node(32)))


    actual = tree_intersection(tree1, tree2)
    expected = "no repeat"
    assert actual == expected

