# [8.6] Towers of Hanoi: In the classic problem of the Towers
# of Hanoi, you have 3 towers and N disks of different sizes
# which can slide onto any tower. The puzzle starts with disks
# sorted in ascending order of size from top to bottom (i.e.
# each disk sits on top of an even larger one). You have the 
# following constraints:

# (1) Only one disk can be moved at a time
# (2) A disk is slid off the top of one tower onto another
# (3) A disk cannot be placed on top of a smaller disk

# Write a program to move the disks from the first tower to the
# last using stacks.

import unittest

def hanoi(towers, n, start, temp, end):
    if n > 0:
        hanoi(towers, n-1, start, end, temp)
        if towers[start]:
            disk = towers[start].pop()
            towers[end].append(disk)
        hanoi(towers, n-1, temp, start, end)
    

class Test(unittest.TestCase):
    def setUp(self):
        self.towers = [[5,4,3,2,1], [], []]
        self.result = [[], [], [5,4,3,2,1]]
    
    def test(self):
        hanoi(self.towers, len(self.towers[0]), 0, 1, 2)
        self.assertEqual(self.towers, self.result)

if __name__ == '__main__':
    unittest.main()

