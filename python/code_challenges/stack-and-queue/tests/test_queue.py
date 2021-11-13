from stack_and_queue.Queue import Queue
import pytest


def test_enqueue_into_a_queue(queue):

    expected = "38"
    actual = queue.rear.value

    assert expected == actual


def test_peek():
    """
    Testing enqueue method for a queue
    """
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(5)


    expected = 1
    actual = queue.peek()

    assert expected == actual


def test_enqueue_multiple_values_queue():

    queue = Queue()

    queue.enqueue(401)
    assert 401 == queue.rear.value

    queue.enqueue(301)
    assert 301 == queue.rear.value


def test_dequeue(queue):
    """
    Testing enqueue method for a queue
    """

    expected = 5
    actual = queue.dequeue()

    assert expected == actual


def test_empty_a_stack_after_multiple_pops(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    expected = True
    assert expected == queue.is_empty()


def test_instantiate_an_empty_stack():
    """
    Testing is_empty method for a queue
    """
    queue = Queue()
    expected = True
    actual = queue.is_empty()
    assert expected == actual


def test_pop_or_peek_on_empty_stack_raises_exception():
    with pytest.raises(Exception):
        stack = Queue()
        stack.peek()
    with pytest.raises(Exception):
        stack = Queue()
        stack.dequeue()


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue("issa")
    queue.enqueue("38")
    return queue
