# [5.5] Debugger: Explain what the following code does:
# ((n & (n-1)) == 0)

# n & (n-1) removes the most least significant 1
# if the result is zero, means there was only one
# one-bit. This means the number was a power of two

import unittest

def check_power_of_two(n):
    return ((n & (n-1)) == 0)

class Test(unittest.TestCase):
    
    def test_check_power_of_two(self):
        self.assertTrue(check_power_of_two(2))
        self.assertTrue(check_power_of_two(4))
        self.assertTrue(check_power_of_two(8))
        self.assertTrue(check_power_of_two(16))

        self.assertFalse(check_power_of_two(3))
        self.assertFalse(check_power_of_two(5))
        self.assertFalse(check_power_of_two(9))
        self.assertFalse(check_power_of_two(17))


if __name__ == '__main__':
    unittest.main()