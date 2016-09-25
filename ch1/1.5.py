# [1:5]. One Away: There are three types of edits that can be
# performed on strings: insert a character, remove a character,
# or replace a character. Given two strings, write a function
# to check if they are one edit (or zero edits) away.
 
# Time complexity: O(n). Where n is the shorter string
# Space complexity: O(1). only creating pointers and a counter 
 
import unittest
 
def one_away(s1, s2):
    if s1 == s2:
        return True
    elif len(s1) == len(s2):
        return equal_size(s1, s2)
    elif abs(len(s1) - len(s2)) > 1:
        return False
    elif len(s1) > len(s2):
        larger = s1
        smaller = s2
    else:
        larger = s2
        smaller = s1
 
    return unequal_size(larger, smaller)
 
def equal_size(s1, s2):
    chars_off = 0
    for i, char in enumerate(s1):
        if char != s2[i]:
            chars_off += 1
 
        if chars_off > 1:
            return False
 
    return True
 
def unequal_size(larger, smaller):
    chars_off = 0
    small_index = 0
    large_index = 0
    while small_index < len(smaller): 
        if larger[large_index] != smaller[small_index]: 
            chars_off += 1 
            large_index += 1 
        else: 
            large_index += 1 
            small_index += 1 
            
        if chars_off > 1:
            return False
 
    return True
 
 
class Test(unittest.TestCase):
    def test_one_away(self):
        self.assertTrue(one_away('one','onef'))
        self.assertTrue(one_away('one','one'))
        self.assertTrue(one_away('one','onf'))
        self.assertTrue(one_away('on','onf'))
        self.assertTrue(one_away('','o'))
 
        self.assertFalse(one_away('one','two'))
        self.assertFalse(one_away('one','onerr'))
        self.assertFalse(one_away('blah','blabber'))
     
         
if __name__ == "__main__":
    unittest.main()