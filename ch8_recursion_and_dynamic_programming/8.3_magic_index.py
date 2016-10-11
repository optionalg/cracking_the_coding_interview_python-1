# [8.3] Magic Index: A magic index in an array A[0...n-1] is
# defined to be an index such that A[i] = i. Given a sorted
# array of distinct integers, write a method to find a magic
# index, if one exists, in array A.

# FOLLOW UP: What if the values are not distinct?

import unittest

def find_magic_index(arr):
    return find_magic_index_helper(arr, 0, len(arr))

def find_magic_index_helper(arr, start, end):

    if end < start:
        return False
    
    mid = (start + end) / 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return find_magic_index_helper(arr, mid+1, end)
    else:
        return find_magic_index_helper(arr, start, mid-1)

def find_magic_index_not_distinct(arr):
    return find_magic_index_not_distinct_helper(arr, 0, len(arr))

def find_magic_index_not_distinct_helper(arr, start, end):
    if end < start or start == len(arr):
        return False
    
    mid = (start + end) / 2
    
    if arr[mid] == mid:
        return mid
    else:
        return (
            find_magic_index_not_distinct_helper(arr, mid+1, end) 
            or 
            find_magic_index_not_distinct_helper(arr, start, mid-1)
        )


class Test(unittest.TestCase):
    
    def test_find_magic_index(self):
        self.assertEqual(find_magic_index([0,2,3,4]), 0)
        self.assertEqual(find_magic_index([-1,0,1,3]), 3)
        self.assertEqual(find_magic_index([-2,1,4,5,6,7]), 1)
        self.assertEqual(find_magic_index([-2,2,4,5,6,7]), False)

    def test_find_magic_index(self):
        self.assertEqual(find_magic_index_not_distinct([0,0,0,0]), 0)
        self.assertEqual(find_magic_index_not_distinct([0,0,3,3]), 3)
        

if __name__ == '__main__':
    unittest.main()

