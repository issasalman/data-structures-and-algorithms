from stack_and_queue.Node import Node
from stack_and_queue.Queue import Queue


class Animal_Shelter:
    """
    Shelter Class For Only Cats and Dogs


    """

    def __init__(self):
        self.dog=Queue()
        self.cat=Queue()


    def enqueue(self, animal):
        """
        to add an item to the rear.
        """
        if (animal =='dog') :
            self.dog.enqueue(animal)
            return animal
        elif (animal == 'cat'):
            self.cat.enqueue(animal)
            return animal
        else:
            return 'We only accept dogs and cats'


    def dequeue(self,pref):
        """
        to remove an item from the front
        """
        if pref.lower() == 'dog':

            if self.dog.is_empty():
                raise Exception("empty")
            else:
                return self.dog.dequeue()
        elif (pref.lower() == 'cat') :


            if self.cat.is_empty():
                raise Exception("empty")
            else:

                return self.cat.dequeue()
        else:
            return None




if __name__ == '__main__':

    x=Animal_Shelter()
    x.enqueue("dog")
    x.enqueue("cat")

    print(x.dequeue("Dog"))

    print(x.dequeue("cat"))




