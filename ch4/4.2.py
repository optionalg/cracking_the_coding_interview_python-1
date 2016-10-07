# [4.2] Minimal Tree: Given a sorted(increasing order)
# array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height

# Space complexity:
# Time complexity:

import unittest


def create_bst(array):
    if not array:
        return None
    elif len(array) == 1:
        return TreeNode(array[0])

    n = len(array)
    head_node = TreeNode(array[n/2])
    left_child = create_bst(array[:n/2])
    right_child = create_bst(array[n/2 + 1:])
    
    head_node.left = left_child
    head_node.right = right_child

    return head_node

class Test(unittest.TestCase):
    
    def test_create_bst(self):
        bst = create_bst([2,3,4,5,6,7])
        self.assertEqual(bst.value, 5)
        self.assertEqual(bst.left.value, 3)
        self.assertEqual(bst.left.left.value, 2)
        self.assertEqual(bst.left.right.value, 4)
        self.assertEqual(bst.right.value, 7)
        self.assertEqual(bst.right.left.value, 6)
        
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
if __name__ == '__main__':
    unittest.main()

