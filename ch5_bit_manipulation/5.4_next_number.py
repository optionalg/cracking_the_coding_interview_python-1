# [5.4] Next Number: Given a positive integer, print the next
# smallest and the next largest number that have the same number
# of 1 bits in their binary representation.

import unittest

def get_next_bin_same_ones(num):
    higher_bin = higher_bin_same_ones(num)
    lower_bin = lower_bin_same_ones(num)
    return (lower_bin, higher_bin)

def higher_bin_same_ones(num):
    count_zeros = 0
    count_ones = 0
    current_bit = num & 1

    while count_ones == 0 or current_bit == 1:
        if current_bit == 1:
            count_ones += 1
        else:
            count_zeros += 1

        current_bit = (num >> count_ones + count_zeros) & 1
        
    pos = count_ones + count_zeros
    flipped_num = (1 << pos ^ num)
    cleared_num = flipped_num & (~0 << pos)
    ones_mask = (1 << (count_ones - 1) ) - 1
    return cleared_num | ones_mask

def lower_bin_same_ones(num):
    count_zeros = 0
    count_ones = 0
    current_bit = num & 1

    while count_zeros == 0 or current_bit == 0:
        if current_bit == 1:
            count_ones += 1
        else:
            count_zeros += 1

        current_bit = (num >> count_ones + count_zeros) & 1
        
    pos = count_ones + count_zeros
    flipped_num = (1 << pos) ^ num
    cleared_num = flipped_num & (~0 << pos)
    ones_mask = (1 << (count_ones + 1) ) - 1
    ones_mask_shifted = (ones_mask << (pos - (count_ones + 1)))
    return cleared_num  | ones_mask_shifted

class Test(unittest.TestCase):
    
    def test_higher_bin_same_ones(self):
        self.assertEqual(higher_bin_same_ones(39), 43)
        self.assertEqual(higher_bin_same_ones(10), 12)
        self.assertEqual(higher_bin_same_ones(60), 71)

    def test_lower_bin_same_ones(self):
        self.assertEqual(lower_bin_same_ones(39), 30)
        self.assertEqual(lower_bin_same_ones(60), 58)

    def test_get_next_bin_same_ones(self):
        self.assertEqual(get_next_bin_same_ones(39), (30, 43))
        self.assertEqual(get_next_bin_same_ones(60), (58, 71))


if __name__ == '__main__':
    unittest.main()