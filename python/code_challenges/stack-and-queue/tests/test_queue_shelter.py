from stack_and_queue.stack_queue_animal_shelter import Animal_Shelter ,Dog,Cat
import pytest




def test_enqueue_dog():
    """
    Testing enqueue method for a queue
    """

    animal=Animal_Shelter()
    Alex=Dog("Alex")

    expected = "Alex"
    actual =animal.enqueue(Alex)

    assert expected == actual


def test_enqueue_cat():
    """
    Testing enqueue method for a queue
    """
    animal=Animal_Shelter()
    Lucy=Cat("Lucy")

    actual =animal.enqueue(Lucy)
    expected = "Lucy"
    assert expected == actual


#




def test_dequeue_cat():
    """
    Testing dequeue method for a queue
    """
    animal=Animal_Shelter()
    Lucy=Cat("Lucy")

    animal.enqueue(Lucy)

    expected = "Lucy"
    actual = animal.dequeue("cat")

    assert expected == actual



def test_dequeue_dog():
    """
    Testing dequeue method for a queue
    """
    animal=Animal_Shelter()
    Billy=Dog("Billy")

    animal.enqueue(Billy)

    expected = "Billy"
    actual = animal.dequeue("dog")

    assert expected == actual


def test_dequeue_other_animals():
    """
    Testing dequeue method for a queue
    """
    animal=Animal_Shelter()

    Billy=Dog("Billy")
    animal.enqueue(Billy)

    Lucy=Cat("Lucy")
    animal.enqueue(Lucy)

    expected = None
    actual = animal.dequeue("wolf")

    assert expected == actual








def test_dequeue_empty_cat():
    """
    Testing dequeue method for a queue
    """
    with pytest.raises(Exception):
        animal=Animal_Shelter()
        Lucy=Cat("Lucy")

        animal.dequeue("cat")


def test_dequeue_empty_dog():
    """
    Testing dequeue method for a queue
    """
    with pytest.raises(Exception):
        animal=Animal_Shelter()
        Billy=Dog("Billy")

        animal.dequeue("dog")




