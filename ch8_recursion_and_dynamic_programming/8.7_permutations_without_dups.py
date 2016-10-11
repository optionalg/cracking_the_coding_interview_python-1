# [8.7] Permutations without Dups: Write a method to compute
# all permutations of a string of unique characters.

import unittest

def perms_with_dups(s):
    if len(s) == 1:
        return [s]

    result = []
    for char_index in range(len(s)):
        active_char = s[char_index]
        remaining = s[:char_index] + s[char_index+1:]
        remaining_perms = perms_with_dups(remaining)
        perms = [active_char + perm for perm in remaining_perms]
        result.extend(perms) 

    return result

class Test(unittest.TestCase):
    
    def setUp(self):
        self.result = ['abc','acb','bac','bca','cab','cba']

    def test_perms_with_dups(self):
        self.assertEqual(set(perms_with_dups('abc')), set(self.result))


if __name__ == '__main__':
    unittest.main()

