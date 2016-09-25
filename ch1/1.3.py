# 1.3. URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold
# the additional characters, and that you are given the "true" length of
# the string. 
 
# Input: "Mr John Smith", 13
# Output: "Mr%20John%20Smith"
 
# Time complexity: O(n) goes through each char in string
# Space complexity: O(n + 2k) creating new list and for each
#                   space will add two additional chars
#                   e.g. ' ' will become '%20'
 
import unittest
 
def urlify(s, l):
    return ''.join(['%20' if char == " " else char for char in s])
 
def urlify2(s, l):
    return '%20'.join(s.split(' '))
 
class Test(unittest.TestCase):
    def test_url(self):
        self.assertEqual(urlify("Mr John Smith", 13), "Mr%20John%20Smith")
        self.assertEqual(urlify("he lloo", 6), "he%20lloo")
        self.assertEqual(urlify("he lloo ", 6), "he%20lloo%20")
 
        self.assertEqual(urlify2("Mr John Smith", 13), "Mr%20John%20Smith")
        self.assertEqual(urlify2("he lloo", 6), "he%20lloo")
        self.assertEqual(urlify2("he lloo ", 6), "he%20lloo%20")
        self.assertEqual(urlify2(" he lloo ", 6), "%20he%20lloo%20")
 
if __name__ == "__main__":
    unittest.main()