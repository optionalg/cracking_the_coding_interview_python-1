# [5.3] Flip Bit to Win: You have an integer and you can 
# flip exactly one bit from a 0 to a 1. Write code to find 
# the length of the longest sequence of 1s you could create.

import unittest

def find_longest_sequence(num):
    previous = 0
    current_run = 0
    current_max = 1

    while num:
        current_bit = num & 1
        num = num >> 1

        if current_bit == 1:
            current_run += 1
        else:
            previous = current_run
            current_run = 0

        current_max = max(current_max, previous + current_run + 1)

    return current_max

class Test(unittest.TestCase):
    
    def test_find_longest_sequence(self):
        self.assertEqual(find_longest_sequence(39), 4)
        self.assertEqual(find_longest_sequence(50), 3)
        self.assertEqual(find_longest_sequence(333), 4)


if __name__ == '__main__':
    unittest.main()