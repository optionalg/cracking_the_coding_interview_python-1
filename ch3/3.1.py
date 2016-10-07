# [3.1] Three in One: Describe how you could use a single
# array to implement three stacks. 

import unittest

class TripleStack(object):
    def __init__(self, each_capacity):
        self.capacity = [each_capacity]*3
        self.stacks = [None]*(3*each_capacity)
        self.stack_tops = [None]*3
        self.space_used = [0]*3

    def push(self, stack_pos, value):
        if self.space_used[stack_pos] >= self.capacity[stack_pos]:
            raise IndexError("Stack doesn't support that index")

        memory_pos = stack_pos*self.capacity[stack_pos] + self.space_used[stack_pos]
        self.stacks[memory_pos] = value
        self.stack_tops[stack_pos] = value
        self.space_used[stack_pos] += 1

    def pop(self, stack_pos):
        if self.space_used[stack_pos] == 0:
            raise IndexError("Pop from empty stack")

        memory_pos = stack_pos*self.capacity[stack_pos] + self.space_used[stack_pos]
        popped_value = self.stacks[memory_pos - 1]
        self.stacks[memory_pos - 1] = None
        self.space_used[stack_pos] -= 1
        self._update_top(stack_pos, memory_pos)
        return popped_value

    def peek(self, stack_pos):
        return self.stack_tops[stack_pos]        

    def _update_top(self, stack_pos, memory_pos):
        if self.space_used[stack_pos] == 0:
            self.stack_tops[stack_pos] = None
        else:
            self.stack_tops[stack_pos] = self.stacks[memory_pos-2]

class Test(unittest.TestCase):
    
    def test_push(self):
        s = TripleStack(5)
        s.push(0,3)
        s.push(1,2)
        s.push(1,5)
        self.assertEqual(s.stacks[0], 3)
        self.assertEqual(s.stacks[5], 2)
        self.assertEqual(s.stacks[6], 5)

    def test_pop(self):
        s = TripleStack(5)
        s.push(0,3)
        s.push(1,2)
        s.push(1,5)
        self.assertEqual(s.pop(0), 3)
        self.assertEqual(s.pop(1), 5)
        self.assertEqual(s.pop(1), 2)
        self.assertRaises(IndexError, s.pop, 1)

    def test_peek(self):
        s = TripleStack(5)
        s.push(0,3)
        s.push(1,2)
        s.push(2,5)
        s.push(2,6)
        self.assertEqual(s.peek(0), 3)
        self.assertEqual(s.peek(1), 2)
        self.assertEqual(s.peek(2), 6)
        
if __name__ == '__main__':
    unittest.main()

