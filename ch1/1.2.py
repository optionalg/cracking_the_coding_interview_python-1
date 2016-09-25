# Time complexity: O(n + m), must go through all characters for both strings
# Space complexity: O(c), hash table will be size of available chars
 
import unittest
 
def check_permutation(s1, s2):
 
    # if lengths are different, cannot be a permutation
    # assuming we are counting ' ' as a separate char
    if len(s1) != len(s2):
        return False
 
    s1_count = char_count(s1)
    s2_count = char_count(s2)
 
    for char in s1_count:
        # if a char in s1 is not in s2, cannot be a permutation
        if not char in s2_count:
            return False
        #if the count of a char is different, cannot be a permutation
        elif s1_count[char] != s2_count[char]:
            return False
 
    # if all the chars were in char1 and char2 and the counts were the same
    # must be a permutation
    return True
 
def char_count(s):
    char_counter = {}
    for char in s:
        # if char not in hash table, add it
        if not s in char_counter:
            char_counter[char] = 1
        # if char in hash table, increment it by one
        else:
            char_counter[char] += 1
 
    return char_counter
 
class Test(unittest.TestCase):
     
    def test_permutation(self):
        self.assertTrue(check_permutation('abcde','edcba'))
        self.assertTrue(check_permutation('',''))
        self.assertTrue(check_permutation('banana', 'ananab'))
 
        self.assertFalse(check_permutation('banana', 'cat'))
        self.assertFalse(check_permutation('bat', 'cat'))
 
 
if __name__ == "__main__":
    unittest.main()