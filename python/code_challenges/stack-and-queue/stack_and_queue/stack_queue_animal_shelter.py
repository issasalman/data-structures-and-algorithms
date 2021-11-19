from stack_and_queue.Queue import Queue

class Cat:

    def __init__(self,name):
        self.name=name
        self.type='cat'

class Dog:

    def __init__(self,name):
        self.name= name
        self.type='dog'

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
        if (animal.type == "dog") :
            self.dog.enqueue(animal.name)
            return animal.name
        elif (animal.type ==  "cat"):
            self.cat.enqueue(animal.name)
            return animal.name
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

    animal=Animal_Shelter()
    Alex=Dog("Alex")
    Billy=Dog("Billy")
    Lucy=Cat("Lucy")
    Kitty=Cat("Kitty")

    animal.enqueue(Alex)
    animal.enqueue(Billy)

    animal.enqueue(Lucy)
    animal.enqueue(Kitty)

    print(animal.dequeue("Dog"))
    print(animal.dequeue("dog"))

    print(animal.dequeue("cat"))
    print(animal.dequeue("cat"))












