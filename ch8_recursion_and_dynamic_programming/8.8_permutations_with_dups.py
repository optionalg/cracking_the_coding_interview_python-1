# [8.8] Permutation with Dups: Write a method to computer all
# permutations of a string whose characters are not necessarily
# unique. The list of permutations should not have duplicates.

import unittest

def perms_with_dups(s):
    char_count = get_char_count(s)
    result = []
    perms_with_dups_helper('', char_count, len(s), result)
    return result

def perms_with_dups_helper(s, char_count, n, result):
    if len(s) == n:
        result.append(s)

    for char in char_count:

        if char_count[char] == 1:
            del char_count[char]
        else:
            char_count[char] -= 1

        perms_with_dups_helper(s + char, char_count, n, result)

        if not char in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1


def get_char_count(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count

class Test(unittest.TestCase):
    
    def setUp(self):
        self.result = ['aaac', 'aaca', 'acaa', 'caaa']

    def test_perms_with_dups(self):
        self.assertEqual(set(perms_with_dups('aaac')), set(self.result))


if __name__ == '__main__':
    unittest.main()

