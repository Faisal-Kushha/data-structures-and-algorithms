from stack_and_queue.stack_queue import Queue


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self):

        if self.rear == "cat":
            self.cat.enqueue()
        elif self.rear == "dog":
            self.dog.enqueue()

    def dequeue(self, pref=None):
        if pref == "cat":
            return self.cat.dequeue()
        elif pref == "dog":
            return self.dog.dequeue()
        else:
            return None


if __name__ == "__main__":

    animalShelter = AnimalShelter()
