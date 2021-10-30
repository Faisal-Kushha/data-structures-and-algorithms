from stack_and_queue.stack_queue import Queue


class AnimalShelter:
    """
    Animal Shlter class which have two method:
     1- enqueue method that will take:
     Arguments: animal and it can be either a dog or a cat object.
    based on that it will add the animal to the animal shelter
     2- dequeue method that will taek:
     Arguments: pref and it can be either "dog" or "cat"
    Return: either a dog or a cat, based on preference. If pref is not "dog" or "cat" then return null.
    """

    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, value):

        if value == "cat":
            self.cat.enqueue("cat")
        elif value == "dog":
            self.dog.enqueue("dog")

    def dequeue(self, pref=None):
        if pref == "cat":
            return self.cat.dequeue()
        elif pref == "dog":
            return self.dog.dequeue()
        else:
            return None


if __name__ == "__main__":

    animalShelter = AnimalShelter()
