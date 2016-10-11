# [8.1] Triple Step: A child is running up a staircase with n
# steps and can hop either 1 step, 2 steps, or 3 steps at a 
# time. Implement a method to count how many possible ways
# the child can run up the stairs.

import unittest

def fib(n):
    if n < 1:
        raise ValueError('Must be positive Integer')
    elif n < 3:
        return 1
    elif n < 4:
        return 2
    else:
        a = 1
        b = 1
        c = 2
        d = 4

        for i in xrange(n-4):
            a = b
            b = c
            c = d
            d = a + b + c

        return d

def fib_r(n):
    memo = {}
    return fib_r_helper(n, memo)

def fib_r_helper(n, memo):
    if n in memo:
        return memo[n]

    if n < 1:
        raise ValueError('Must be positive Integer')
    elif n < 3:
        return 1
    elif n < 4:
        return 2
    else:
        result = fib_r(n-1) + fib_r(n-2) + fib_r(n-3)
        memo[n] = result
        return result



class Test(unittest.TestCase):
    
    def test_fib(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 4)
        self.assertEqual(fib(5), 7)
        self.assertEqual(fib(6), 13)
        self.assertRaises(ValueError, fib, -1)

    def test_fib_r(self):
        self.assertEqual(fib_r(1), 1)
        self.assertEqual(fib_r(2), 1)
        self.assertEqual(fib_r(3), 2)
        self.assertEqual(fib_r(4), 4)
        self.assertEqual(fib_r(5), 7)
        self.assertEqual(fib_r(6), 13)
        self.assertRaises(ValueError, fib_r, -1)



if __name__ == '__main__':
    unittest.main()

