# [8.9] Parens: Implement an algorithm to print all valid (e.g
# properly opened and closed) combinations of n pairs of
# parentheses

# EXAMPLE: 
# Input: 3
# Output: ((())), (()()), (())(), ()(()), ()()()

import unittest

def parens(n):
    result = []
    parens_helper('', 0, 0, n, result)
    return result

def parens_helper(s, left, right, n, result):
    if left == n and right == n:
        result.append(s)

    if left < n:
        parens_helper(s + '(', left+1, right, n, result)

    if right < left:
        parens_helper(s + ')', left, right+1, n, result)


class Test(unittest.TestCase):
    def setUp(self):
        self.result = ['((()))', '(())()', '()()()', '()(())', '()()()', '(()())']
    
    def test_parents(self):
        self.assertEqual(set(parens(3)), set(self.result))


if __name__ == '__main__':
    unittest.main()

