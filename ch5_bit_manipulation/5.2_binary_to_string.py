# [5.2] Binary to String: Given a real number between 0 and 1
# (e.g., 0.72) that is passed in as a double, print the binary
# representation. If the number cannot be represented accurately
# in binary with at most 32 characters, print "ERROR"

import unittest

def bin_to_string(num):
    result = []
    while num and len(result) <= 32:
        num *= 2
        if num >= 1:
            result.append('1')
            num -= 1
        else:
            result.append('0')

    if len(result) > 32:
        raise ValueError('Binary cannot be represented with 32 bits')

    return '.' + ''.join(result)


class Test(unittest.TestCase):
    
    def test_bin_to_string(self):
        self.assertEqual(bin_to_string(.5), '.1')
        self.assertEqual(bin_to_string(.25), '.01')
        self.assertEqual(bin_to_string(.125), '.001')
        self.assertEqual(bin_to_string(.625), '.101')
        self.assertRaises(ValueError, bin_to_string, .1)

if __name__ == '__main__':
    unittest.main()