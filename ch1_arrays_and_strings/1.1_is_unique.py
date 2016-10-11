# Time complexity: O(n) because needs to check each character
# Space complexity: O(c) where c is each character
 
import unittest
 
def is_unique(s):
    # create a hashmap to keep track of char count
    char_count = {}
 
    for char in s:
        # if character is not in hashmap add it
        if not char in char_count:
            char_count[char] = 1
        else:
            # if char is in hashmap, means there is a duplicate character
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
