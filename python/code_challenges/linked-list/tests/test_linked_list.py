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
    ll.append(3)
    expected = "value added"
    actual = ll.append(3)
    assert expected == actual

def test_head_pointing_to_next_node():
    ll = LinkedList()
    ll.append(3)
    expected = 'head -> 3 -> None'
    actual = ll.__str__()
    assert expected == actual


def test_multi_values_added(ll):
    ll.append(True)
    expected = 4
    actual = ll.countering()
    assert expected == actual




def test_all_values_in_LL(ll):
    expected = 'head -> 10 -> Issa -> 500 -> None'
    actual = ll.__str__()
    assert expected == actual




def test_value_found(ll):

    expected = True
    actual = ll.search("Issa")
    assert expected == actual

def test_value_not_found(ll):

    expected = False
    actual = ll.search(7)
    assert expected == actual




@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(10)
    ll.append('Issa')
    ll.append(500)

    return ll
