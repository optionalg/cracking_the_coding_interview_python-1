import unittest

def is_rotation(s1, s2):
    return len(s1) == len(s2) and is_substring(s1, s2+s2)

def is_substring(s1, s2):
    return s1 in s2

class Test(unittest.TestCase):
    s1A = 'cat'
    s2A = 'hat'

    s1B = 'catch'
    s2B =  'tchca'

    s1C = 'pokemon'
    s2C =  'monapoke'

    def test_is_rotation(self):
        self.assertFalse(is_rotation(Test.s1A, Test.s2A))
        self.assertTrue(is_rotation(Test.s1B, Test.s2B))
        self.assertFalse(is_rotation(Test.s1C, Test.s2C))

if __name__ == '__main__':
    unittest.main()
