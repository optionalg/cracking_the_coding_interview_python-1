# [5.1] Insertion: You are given two 32-bit numbers, N and M, and
# two bit positions, i and j. Write a method to insert M into N
# such that M starts at bit j and ends at bit i. You can assume that 
# the bits j and i have enough space to fit all of M. That is, if
# M = 1011, you can assume that there are at least 5 bits between j
# and i. You would not, for example, have j =3 and i =2, because M 
# could not fully fit between bit 3 and bit 2.

# EXAMPLE
# Input: N = 10000000000, M = 10011, i = 2, j = 6
# Output: N = 10001001100


import unittest

def insert_N_into_M(N, M, i, j):
    N_num = int(N, 2)
    M_num = int(M, 2)

    n_mask = (~0 << (j + 1)) | ((1 << i) - 1)
    n_cleared = N_num & n_mask
    m_shifted = M_num << i
    result = n_cleared | m_shifted

    return int_to_binary_string(result)

def int_to_binary_string(num):
    return bin(num)[2:]

class Test(unittest.TestCase):
    
    def setUp(self):
        self.N = '10000000000'
        self.M = '10011'
        self.i = 2
        self.j = 6

    def test_insert_N_into_M(self):
        self.assertEqual(
            insert_N_into_M(self.N, self.M, self.i, self.j),
            '10001001100'
        )

if __name__ == '__main__':
    unittest.main()