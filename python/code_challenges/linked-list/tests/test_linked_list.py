from linked_list import __version__
from linked_list.linked_list import LinkedList, Node

import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual

def test_inserting_one_value():
    ll = LinkedList()
    ll.insert(3)
    expected = "value added"
    actual = ll.insert(3)
    assert expected == actual

def test_head_pointing_to_next_node():
    node = Node(10)
    expected = 10
    actual = node.value
    assert actual == expected


def test_multi_values_added(ll):
    expected = 3
    actual = ll.countering()
    assert expected == actual




def test_all_values_in_LL(ll):
    expected = 'head -> [10] -> [30] -> [500] -> None'
    actual = ll.__str__()
    assert expected == actual




def test_value_found(ll):

    expected = False
    actual = ll.includes("Issa")
    assert expected == actual

def test_value_not_found(ll):

    expected = True
    actual = ll.includes(10)
    assert expected == actual


def test_insert_before(ll):
    ll.insert_before(30,40)
    expected = 'head -> [10] -> [40] -> [30] -> [500] -> None'
    actual = ll.__str__()
    assert expected == actual


def test_insert_after(ll):
    ll.insert_after(30,40)
    expected = 'head -> [10] -> [30] -> [40] -> [500] -> None'
    actual = ll.__str__()
    assert expected == actual




@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(10)
    ll.append(30)
    ll.append(500)

    return ll
