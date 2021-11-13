from stack_and_queue.Stack import Stack
import pytest


def test_push_onto_a_stack(stack):
    actual = stack.top.value
    expected = "34"
    assert expected == actual


def test_push_multiple_values_stack():

    stack = Stack()

    stack.push(401)
    assert 401 == stack.top.value

    stack.push(301)
    assert 301 == stack.top.value


def test_pop(stack):
    actual = stack.pop()
    expected = "34"
    assert expected == actual


def test_empty_a_stack_after_multiple_pops(stack):
    stack.pop()
    stack.pop()
    stack.pop()

    expected = True
    assert expected == stack.is_empty()


def test_peek_stack():
    """
    Testing push method for a stack
    """
    stack = Stack()
    stack.push(1)
    stack.push(5)


    expected = 5
    actual = stack.peek()

    assert expected == actual


def test_instantiate_an_empty_stack():
    """
    Testing is_empty method for a stack
    """
    stack = Stack()
    expected = True
    actual = stack.is_empty()
    assert expected == actual


def test_pop_or_peek_on_empty_stack_raises_exception():
    with pytest.raises(Exception):
        stack = Stack()
        stack.peek()
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()


@pytest.fixture
def stack():
    stack = Stack()
    stack.push(2)
    stack.push("401-python")
    stack.push("34")
    return stack
