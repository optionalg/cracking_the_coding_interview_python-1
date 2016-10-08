# [5.7] Pairwise Swap: Write a program to swap odd and even bits
# in an integer with as few instructions as possible (e.g., bit
# 0 and bit 1 are swapped, bit 2 and bit 3 and swapped, and so on)

import unittest

def pairwise_swap(num):
    
    even_mask = create_even_mask(num)
    odd_mask = create_odd_mask(num)
    even_cleared = num & even_mask
    odd_cleared = num & odd_mask
    combined = (odd_cleared >> 1) | (even_cleared << 1)
    return (odd_cleared >> 1) | (even_cleared << 1)

def create_odd_mask(num):
    bin_representation = bin(num)[2:]
    bit_length = len(bin_representation)
    bit_sign = '0'
    mask = []

    for i in range(bit_length):
        mask.insert(0, bit_sign)
        bit_sign = '1' if bit_sign =='0' else '0'

    return int(''.join(mask),2)

def create_even_mask(num):
    bin_representation = bin(num)[2:]
    bit_length = len(bin_representation)
    bit_sign = '1'
    mask = []

    for i in range(bit_length):
        mask.insert(0, bit_sign)
        bit_sign = '1' if bit_sign =='0' else '0'

    return int(''.join(mask),2)


class Test(unittest.TestCase):
    
    def test_create_even_mask(self):
        self.assertEqual(create_even_mask(int('111000', 2)), int('010101',2))
        self.assertEqual(create_even_mask(int('1110000', 2)), int('1010101',2))

    def test_create_odd_mask(self):
        self.assertEqual(create_odd_mask(int('111000', 2)), int('101010',2))
        self.assertEqual(create_odd_mask(int('11100110', 2)), int('10101010',2))

    def test_pairwise_swap(self):
        self.assertEqual(pairwise_swap(int('111000',2)), int('110100',2))
        self.assertEqual(pairwise_swap(int('11100111',2)), int('11011011',2))

if __name__ == '__main__':
    unittest.main()

