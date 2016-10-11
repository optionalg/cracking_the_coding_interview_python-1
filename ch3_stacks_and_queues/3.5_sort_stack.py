# [3.5] Sort Stack: Write a program to sort a stack such that
# the smallest items are on the top. You can use an additional
# temporary stack, but you may not copy the elements into
# any other data structure (such as an array). The stack
# supports teh following operations: push, pop, peek, and 
# is_empty

import unittest

def sort_stack(s):
    temp_stack = Stack()

    while not s.is_empty():
        temp_value = s.pop()

        if not temp_stack.is_empty() and temp_stack.peek() > temp_value:
            while not temp_stack.is_empty() and temp_stack.peek() > temp_value:
                s.push(temp_stack.pop())
        
        temp_stack.push(temp_value)

    while not temp_stack.is_empty():
        s.push(temp_stack.pop())

    return s

class Stack(object):
    
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return None

        return self.stack[-1]

    def is_empty(self):
        return not self.stack


class Test(unittest.TestCase):
    
    def test_sort_stack(self):
        s = Stack()
        s.stack = [2,3,4]
        self.assertEqual(sort_stack(s).stack,[4,3,2])

        s2 = Stack()
        s2.stack = [3,8,4,3,7]
        self.assertEqual(sort_stack(s2).stack,[8,7,4,3,3])

        s3 = Stack()
        s3.stack = []
        self.assertEqual(sort_stack(s3).stack,[])
        
if __name__ == '__main__':
    unittest.main()

