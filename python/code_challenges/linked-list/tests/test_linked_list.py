from linked_list import __version__
from linked_list.linked_list import LinkedList, Node,zipLists

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
    ll.insert_before(10,40)
    expected = 'head -> [40] -> [10] -> [30] -> [500] -> None'
    actual = ll.__str__()
    assert expected == actual




def test_insert_after(ll):
    ll.insert_after(30,40)
    expected = 'head -> [10] -> [30] -> [40] -> [500] -> None'
    actual = ll.__str__()
    assert expected == actual


def test_greater_than_the_length(ll):

    expected = 'k is greater than the length of the linked list'
    actual =  ll.kthFromEnd(10)
    assert expected == actual


def test_k_and_the_length_of_the_list_are_the_same(ll):
    expected = 10
    actual =  ll.kthFromEnd(3)
    assert expected == actual


def test_k_is_not_a_positive_integer(ll):
    expected ="Please input positive numbers"
    actual =  ll.kthFromEnd(-3)
    assert expected == actual


def test__linked_list_is_of_a_size_1():
    ll = LinkedList()
    ll.append(3)
    expected =3
    actual =  ll.kthFromEnd(0)
    assert expected == actual


def test__Happy_Pat_K_is_not_in_middle():
    ll = LinkedList()
    ll.append(3)
    ll.append(8)
    ll.append(4)
    ll.append(20)
    ll.append(3)

    assert ll.kthFromEnd(1) == 20
    assert ll.kthFromEnd(2) == 4
    assert ll.kthFromEnd(3) == 8


def test__merging():
    ll = LinkedList()
    ll2 = LinkedList()

    ll.append(3)
    ll.append(8)
    ll.append(8)

    ll2.append(4)
    ll2.append(20)
    ll2.append(3)
    expected ="head -> [3] -> [4] -> [8] -> [20] -> [8] -> [3] -> None"

    zipLists(ll,ll2)
    actual =   ll.__str__()
    assert expected == actual




@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(10)
    ll.append(30)
    ll.append(500)

    return ll
