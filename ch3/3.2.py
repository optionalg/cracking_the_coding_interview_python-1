# [3.2] Stack Min: How would you design a stack which, 
# in addition to push and pop, has a function min which
# returns the minimum element? Push, pop, and min should
# all operate in O(1) time.

import unittest

class Stack(object):
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min():
            self.min_stack.append(value)

    def pop(self):
        popped_value = self.stack.pop()
        if popped_value == self.min():
            self.min_stack.pop()

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

class Test(unittest.TestCase):
    
    def test_push(self):
        s = Stack()
        s.push(2)
        s.push(5)
        s.push(1)
        self.assertEqual(s.stack, [2,5,1])

    def test_pop(self):
        s = Stack()
        s.push(2)
        s.push(5)
        s.push(1)
        s.push(1)
        s.pop()
        s.pop()
        self.assertEqual(s.stack, [2,5])

    def test_min(self):
        s = Stack()
        s.push(2)
        s.push(5)
        s.push(1)
        self.assertEqual(s.min(), 1)

        s2 = Stack()
        s2.push(2)
        s2.push(5)
        s2.push(1)
        s2.push(1)
        s2.pop()
        s2.pop()
        self.assertEqual(s2.min(), 2)
        
if __name__ == '__main__':
    unittest.main()

