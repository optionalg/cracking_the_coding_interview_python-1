# [8.14] Boolean Evaluation: Given a boolean expression 
# consisting of the symbols 0 (false), 1 (true), &
# (AND), | (OR), and ^ (XOR), and a desired boolean result
# value 'result', implement a function to count the number
# of ways of parenthesizing the expression such that it
# evaluates to 'result'. The expression should be
# fully parenthesize (e.g., (0)^(1)) but not extraneously
# (e.g., (((0))^(1))).

# EXAMPLE
# countEval("1^0|0|1", False) -> 2
# countEval("0&0&0&1^1|0", True) -> 10

import unittest

def bool_eval(expr, result):
    
    if expr == "1":
        if result:
            return 1
        return 0
    if expr == "0":
        if not result:
            return 1
        return 0

    subways = 0

    for i in xrange(1,len(expr),2):
        
        operator = expr[i]
        left = expr[0:i]
        right = expr[i+1:]

        left_true = bool_eval(left, True)
        left_false = bool_eval(left, False)
        right_true = bool_eval(right, True)
        right_false = bool_eval(right, False)
        total_ways = (left_true + left_false) * (right_true + right_false)
        true_ways = 0

        if operator == "&":
            true_ways += left_true*right_true
        elif operator == "|":
            true_ways += (
                (left_true*right_true) 
                + (left_true*right_false) 
                + (left_false*right_true)
            )
        elif operator == "^":
            true_ways += (left_true*right_false) + (left_false*right_true)

        if result:
            subways += true_ways
        else:
            subways += total_ways - true_ways

    return subways
    
class Test(unittest.TestCase):

    def test_bool_eval(self):
        self.assertEqual(bool_eval("0&0&0&1^1|0", True), 10)
        self.assertEqual(bool_eval("1^0|0|1", False), 2)
        
if __name__ == '__main__':
    unittest.main()