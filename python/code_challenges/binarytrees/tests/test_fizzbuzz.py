from binarytrees.fizzbuzztree import fizz_buzz , karyNode ,fizz_buzz_tree,karyTree
import pytest

def test_fizzbuzztree(tree):
    expected=['1', 'Buzz', 'Fizz', 'Buzz', 'Buzz', 'Buzz', 'FizzBuzz', 'Fizz', 'Fizz']
    actual=(fizz_buzz_tree(tree))
    assert expected == actual

def test_fizzbuzztreeempty():
    tree = karyTree()
    expected="empty tree"
    actual=(fizz_buzz_tree(tree))
    assert expected == actual



def test_buzz():

    actual= fizz_buzz(5)

    expected="Buzz"
    assert expected == actual

def test_fizzt():

    actual= fizz_buzz(3)

    expected="Fizz"
    assert expected == actual

def test_fizzbuzz():

    actual= fizz_buzz(15)

    expected="FizzBuzz"
    assert expected == actual


def test_fizzbuzz_string():

    actual= fizz_buzz(13)

    expected="13"
    assert expected == actual


@pytest.fixture
def tree():
    tree = karyTree()
    tree.root=karyNode(1,[karyNode(20,[karyNode(250),karyNode(35),karyNode(105)]),karyNode(3,[karyNode(333)]),karyNode(10,[karyNode(444)])])


    return tree
