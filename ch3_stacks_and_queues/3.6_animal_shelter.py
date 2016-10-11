# [3.6] Animal Shelter: An animal shelter, which holds
# only dogs and cats, operates on a strictly "first-in,
# first-out" basis. People must adopt either the "oldest"
# (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or
# a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would
# like. Create the data structures to maintain this system
# and implement operations such as enqueue, dequeue_any,
# dequeue_dog, dequeue_cat.


import unittest
from datetime import datetime

class Shelter(object):
    def __init__(self):
        self.cat_queue = []
        self.dog_queue = []

    def enqueue(self, pet):
        pet.enter_date = datetime.now()
        if isinstance(pet, Dog):
            self.dog_queue.append(pet)
        else:
            self.cat_queue.append(pet)

    def cat_dequeue(self):
        if not self.cat_queue:
            raise IndexError("There are no cats")

        return self.cat_queue.pop(0)

    def dog_dequeue(self):
        if not self.dog_queue:
            raise IndexError("There are no dogs")

        return self.dog_queue.pop(0)

    def dequeue_any(self):
        if not self.cat_queue and not self.dog_queue:
            raise IndexError("Shelter is empty")            

        elif not self.cat_queue:
            return self.dog_dequeue()
        elif not self.dog_queue:
            return self.cat_dequeue()
        else:
            first_cat = self.cat_queue[0]
            first_dog = self.dog_queue[0]

            if first_dog.enter_date < first_cat.enter_date:
                adopted_pet = self.dog_dequeue()
            else:
                adopted_pet = self.cat_dequeue()

            return adopted_pet


class Animal(object):
    def __init__(self):
        self.enter_date = None

class Dog(Animal):
    pass
        
class Cat(Animal):
    pass


class Test(unittest.TestCase):
    
    def test_enqueue(self):
        shelter = Shelter()
        cat = Cat()
        dog = Dog()
        shelter.enqueue(cat)
        shelter.enqueue(dog)
        self.assertEqual(shelter.cat_queue[0], cat)
        self.assertEqual(shelter.dog_queue[0], dog)

    def test_dequeue(self):
        shelter = Shelter()
        cat1 = Cat()
        cat2 = Cat()
        dog1 = Dog()
        dog2 = Dog()
        shelter.enqueue(cat1)
        shelter.enqueue(cat2)
        shelter.enqueue(dog1)
        shelter.enqueue(dog2)
        self.assertEqual(shelter.cat_dequeue(), cat1)
        self.assertEqual(shelter.cat_dequeue(), cat2)
        self.assertEqual(shelter.dog_dequeue(), dog1)
        self.assertEqual(shelter.dog_dequeue(), dog2)

    def test_dequeue_any(self):
        shelter = Shelter()
        cat1 = Cat()
        cat2 = Cat()
        dog1 = Dog()
        dog2 = Dog()
        shelter.enqueue(cat1)
        shelter.enqueue(dog1)
        shelter.enqueue(cat2)
        shelter.enqueue(dog2)
        self.assertEqual(shelter.dequeue_any(), cat1)
        self.assertEqual(shelter.dequeue_any(), dog1)
        self.assertEqual(shelter.dequeue_any(), cat2)
        self.assertEqual(shelter.dequeue_any(), dog2)
        
if __name__ == '__main__':
    unittest.main()