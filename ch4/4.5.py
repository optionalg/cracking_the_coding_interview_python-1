# [4.5] Validate BST: Implement a function to check if a
# binary tree is a binary search tree

import unittest


def valid_bst(node):
    return valid_bst_helper(node, float("-inf"), float("inf"))

def valid_bst_helper(node, floor, ceiling):
    if not node:
        return True

    if node.value < floor or node.value > ceiling:
        return False

    left = valid_bst_helper(node.left, floor, node.value)
    right = valid_bst_helper(node.right, node.value, ceiling)
    return left and right


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Test(unittest.TestCase):
    
    def test_valid_bst(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n3.left = n2
        n2.left = n1
        n3.right = n4
        n4.right = n5
        self.assertTrue(valid_bst(n3))
        n6 = TreeNode(6)
        n2.right = n6
        self.assertFalse(valid_bst(n3))
        
        
if __name__ == '__main__':
    unittest.main()

