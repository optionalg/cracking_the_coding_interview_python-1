# [5.6] Conversion: Write a function to determine the number of
# bits you would need to flip to convert integer A to integer B.

# EXAMPLE
# Input: 29 (or: 11101), 15 (or: 01111)
# Output: 2

import unittest

def test_flip_to_make_equal(n1, n2):
    different_bits = n1 ^ n2
    count = 0
    while different_bits:
        different_bits = different_bits & (different_bits - 1)
        count += 1
    return count

class Test(unittest.TestCase):
    
    def test_flip_to_make_equal(self):
        self.assertEqual(test_flip_to_make_equal(29, 15), 2)


if __name__ == '__main__':
    unittest.main()