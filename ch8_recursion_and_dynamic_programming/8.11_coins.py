# [8.11] Coins: Given an infinite number of quarters, dimes, 
# nickels, and pennies, write code to calculate the number of 
# ways of representing n cents.


import unittest

def change(amount):
    coins = [25,10,5,1]
    return change_helper(amount, 0, coins)


def change_helper(amount, denom, coins):
    if denom == 3:
        return 1
    elif amount < 0:
        return 0

    denom_amount = coins[denom]
    subtract_denom = change_helper(amount-denom_amount, denom, coins)
    move_to_next_denom = change_helper(amount, denom+1, coins)
    return subtract_denom + move_to_next_denom

class Test(unittest.TestCase):
    
    def test_change(self):
        self.assertEqual(change(10), 4)
        self.assertEqual(change(15), 6)


if __name__ == '__main__':
    unittest.main()

