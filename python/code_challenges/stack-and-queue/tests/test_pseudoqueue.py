from stack_and_queue.queue_pseudo import Pseudo_queue as pseudo
import pytest



def test_instantiate_an_empty_psuedo():

    with pytest.raises(Exception):
        Pseudo_queue = pseudo()
        Pseudo_queue.dequeue()



def test_push_onto_a_stack_psudo():
    Pseudo_queue = pseudo()
    Pseudo_queue.enqueue(2)
    Pseudo_queue.enqueue("401-python")

    actual =  Pseudo_queue.enqueue("34")
    expected = "34"
    assert expected == actual



def test_str():
    Pseudo_queue = pseudo()
    Pseudo_queue.enqueue(2)
    Pseudo_queue.enqueue("401-python")
    Pseudo_queue.enqueue("34")
    actual =  Pseudo_queue.__str__()
    expected = 'top -> [34] -> [401-python] -> [2] -> None'
    assert expected == actual



def test_pop_psudo():
    Pseudo_queue = pseudo()
    Pseudo_queue.enqueue(2)
    Pseudo_queue.enqueue("401-python")

    actual =  Pseudo_queue.dequeue()
    expected = 2
    assert expected == actual




def test_pop_multi_psudo():
    Pseudo_queue = pseudo()
    Pseudo_queue.enqueue(2)
    Pseudo_queue.enqueue(50)
    Pseudo_queue.enqueue("401-python")

    assert 2 == Pseudo_queue.dequeue()
    assert 50 == Pseudo_queue.dequeue()
    assert "401-python" == Pseudo_queue.dequeue()




@pytest.fixture
def Pseudo_queue():
    Pseudo_queue = pseudo()
    Pseudo_queue.enqueue(2)
    Pseudo_queue.enqueue("401-python")
    Pseudo_queue.enqueue("34")
    return Pseudo_queue
