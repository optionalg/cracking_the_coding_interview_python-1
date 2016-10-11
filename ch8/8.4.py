# [8.4] Power Set: Write a method to return all subsets of
# a set.

import unittest

def get_subsets(a_set):
    if len(a_set) == 1:
        return [set(), a_set]

    current_item = a_set.pop()
    smaller_set = get_subsets(a_set)
    copy_smaller_set = [item.copy() for item in smaller_set]
    
    for item in copy_smaller_set:
        item.add(current_item)

    return copy_smaller_set + smaller_set



class Test(unittest.TestCase):
    
    def setUp(self):
        self.results = get_subsets(set([1,2,3]))
        self.answer = [
            set([]), 
            set([1]),
            set([2]), 
            set([3]),
            set([1, 2]), 
            set([1, 3]), 
            set([2, 3]), 
            set([1, 2, 3])
        ]


    def test_get_subsets(self):
        self.assertEqual(len(self.results), 8)
        self.assertTrue(self.check_lists_equal(self.results, self.answer))


    def check_lists_equal(self, list1, list2):
        if len(list1) != len(list2):
            return False

        for a_set in list1:
            if not a_set in list2:
                return False

        return True


if __name__ == '__main__':
    unittest.main()

