# Time complexity: O(n**2) because loops through all characters for each character
# Space complexity: O(1)
 
import unittest
 
def is_unique(s):
     
    for i, char1 in enumerate(s):
        for j, char2 in enumerate(s):
            if i != j and char1 == char2:
                return False
 
    return True
 
 
class Test(unittest.TestCase):
     
    def test_unique(self):
        self.assertTrue(is_unique('abcdefg'))
        self.assertTrue(is_unique('1234567'))
        self.assertFalse(is_unique('aabcdefg'))
        self.assertFalse(is_unique('123456788'))
 
 
if __name__ == "__main__":
    unittest.main()