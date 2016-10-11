# [8.5] Recursive Multiply: Write a recursive function to
# multiply two positive integers without using the * 
# operator. You can use addition, subtraction, and bit 
# shifting, but you should minimize the number of those
# operations.

#Time and Space Complexity 1: O(k)
#Time and Space Complexity 2: O(log(k))
# k is the smaller integer

import unittest

def r_multiply1(a,b):
    if a == 1:
        return b

    if a < b:
        small = a
        large = b
    else:
        large = a
        small = b

    return r_multiply1(a - 1, b) + b

def r_multiply2(a,b):
    if a < b:
        small = a
        large = b
    else:
        large = a
        small = b

    if small == 1:
        return large

    s = small >> 1
    half_prod = r_multiply2(s, large)

    if small % 2 == 1:
        return half_prod + half_prod + large

    return half_prod + half_prod

class Test(unittest.TestCase):
    
    def test_r_multiply1(self):
        self.assertEqual(r_multiply1(4,2),8)
        self.assertEqual(r_multiply1(4,3),12)
        self.assertEqual(r_multiply1(3,4),12)
        self.assertEqual(r_multiply1(4,1),4)
        self.assertEqual(r_multiply1(1,6),6)

    def test_r_multiply2(self):
        self.assertEqual(r_multiply2(4,2),8)
        self.assertEqual(r_multiply2(4,3),12)
        self.assertEqual(r_multiply2(3,4),12)
        self.assertEqual(r_multiply2(1,6),6)
        self.assertEqual(r_multiply2(4,1),4)
        
if __name__ == "__main__":
    unittest.main()