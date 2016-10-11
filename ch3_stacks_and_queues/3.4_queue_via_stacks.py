# [3.4] Queue via Stacks: Implement a MyQueue class
# which implements a queue using two stacks.

import unittest


class MyQueue(object):
    
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, value):
        self.s1.append(value)

    def pop(self):
        if not self.s1 and not self.s2:
            raise IndexError("pop on empty queue")

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()


class Test(unittest.TestCase):
    
    def test_push(self):
        q = MyQueue()
        for i in xrange(5):
            q.push(i)

        self.assertEqual(q.s1, [0,1,2,3,4])

    def test_pop(self):
        q = MyQueue()
        q.s1 = range(5)
        self.assertEqual(q.pop(),0)
        self.assertEqual(q.s1,[])
        self.assertEqual(q.s2,[4,3,2,1])
        self.assertEqual(q.pop(),1)
        
if __name__ == '__main__':
    unittest.main()

