from stack_and_queue.stack_queue_animal_shelter import Animal_Shelter
import pytest




def test_enqueue_dog():
    """
    Testing enqueue method for a queue
    """
    dog_queue = Animal_Shelter()



    expected = "dog"
    actual =dog_queue.enqueue("dog")

    assert expected == actual


def test_enqueue_cat():
    """
    Testing enqueue method for a queue
    """
    cat_queue = Animal_Shelter()



    expected = "cat"
    actual =cat_queue.enqueue("cat")

    assert expected == actual



def test_enqueue_other():
    """
    Testing enqueue method for a queue
    """
    other_queue = Animal_Shelter()



    expected = 'We only accept dogs and cats'
    actual =other_queue.enqueue("wolf")

    assert expected == actual


def test_dequeue_cat():
    """
    Testing dequeue method for a queue
    """
    cat_queue = Animal_Shelter()
    cat_queue.enqueue("cat")
    expected = "cat"
    actual = cat_queue.dequeue("cat")

    assert expected == actual



def test_dequeue_dog():
    """
    Testing dequeue method for a queue
    """
    dog_queue = Animal_Shelter()
    dog_queue.enqueue("dog")
    expected = "dog"
    actual = dog_queue.dequeue("dog")

    assert expected == actual




def test_dequeue_empty_dog():
    """
    Testing dequeue method for a queue
    """
    with pytest.raises(Exception):
        dog_queue = Animal_Shelter()


        dog_queue.dequeue("dog")



def test_dequeue_empty_cat():
    """
    Testing dequeue method for a queue
    """
    with pytest.raises(Exception):
        cat_queue = Animal_Shelter()


        cat_queue.dequeue("cat")


