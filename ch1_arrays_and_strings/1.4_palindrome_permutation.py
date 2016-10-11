# 1.4. Palindrom Permutation: Given a string, write a function to check 
# if it is a permutation of a palindrome. A palindrome is a word or
# phrase that is the same forwards and backwards. A permutation is a 
# rearrangement of letters. The palindrome does not need to be limited
# to just dictionary words.
 
# Input: Tact Coa
# Output: True
 
# Hash Table Solution
# Time complexity: O(n) count characters and then loop through smaller
# subset
# Space complexity: O(c) where c is each char / Also can be thought
# of as O(1) because set of characters is limited
 
# Bit Vector Solution
# Time complexity: O(n) need to look through each character
# Space complexity: O(1) information all stored in one integer
 
import unittest
 
def palindrome_permutation(s):
    char_count = get_char_count(s)
    odd_count = 0
    
    for char in char_count:
        if odd_count > 1:
            return False
 
        if char_count[char] % 2 == 1:
            odd_count += 1
 
    return True
 
def get_char_count(s):
    char_count = {}
    for char in s:
        if char not in char_count:
             char_count[char] = 1
        else:
            char_count[char] += 1
     
    return char_count
 
def palindrome_permutation2(s):
    bv = [0]*26
    for char in s:
       bv[array_index(char)] = 1^bv[array_index(char)]

    bit_str = [str(b) for b in bv]
    if int(''.join(bit_str),2) & int(''.join(bit_str),2) - 1:
        return False
    else:
        return True
 
def array_index(s):
    return ord(s.lower()) - 97
 
 
 
 
class Test(unittest.TestCase):
    def test_palindrome_permutation(self):
        # hash table solution
        self.assertTrue(palindrome_permutation('abcdeabcde'))
        self.assertTrue(palindrome_permutation('ddddeeeej'))
        self.assertTrue(palindrome_permutation('xyxyxyxyttu'))
        self.assertFalse(palindrome_permutation('abcdeabcdeae'))
        self.assertFalse(palindrome_permutation('aabbcdez'))
        self.assertFalse(palindrome_permutation('xyz'))

        # bit array solution
        self.assertTrue(palindrome_permutation2('abcdeabcde'))
        self.assertTrue(palindrome_permutation2('ddddeeeej'))
        self.assertTrue(palindrome_permutation2('xyxyxyxyttu'))
        self.assertFalse(palindrome_permutation2('abcdeabcdeae'))
        self.assertFalse(palindrome_permutation2('aabbcdez'))
        self.assertFalse(palindrome_permutation2('xyz'))
 
if __name__ == "__main__":
    unittest.main()