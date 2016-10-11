# [4.10] Check Subtree: T1 and T2 and two very large
# binary tree, with T1 much bigger than T2. Create an 
# algorithm to determine if T2 is a subtree of T1.

# A tree T2 is a subtree of T1 if there exists a node
# n in T1 such that the subtree of n is identical to
# T2. That is, if you cut off the tree at node n,
# the two trees would be identical.

import unittest


def is_subtree(bst1, bst2):
    if bool(bst1) ^ bool(bst2):
        return False
    elif not bst1 and not bst2:
        return True

    if bst1.value == bst2.value:
        left_is_subtree = is_subtree(bst1.left, bst2.left)
        right_is_subtree = is_subtree(bst1.right, bst2.right)
        return left_is_subtree and right_is_subtree

    else:
        return (
            is_subtree(bst1, bst2.left) or is_subtree(bst1, bst2.right)
        )


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Test(unittest.TestCase):
    
    def setUp(self):
        self.bst1 = self.create_bst(range(10))
        self.bst2 = TreeNode(4)
        self.n2 = TreeNode(3)
        self.bst2.left = self.n2

        self.bst3 = TreeNode(9)
        self.n10 = TreeNode(10)
        self.bst3.right = self.n10

    def test_is_subtree(self):
        self.assertTrue(is_subtree(self.bst2, self.bst1))
        self.assertFalse(is_subtree(self.bst3, self.bst1))

    def create_bst(self, array):
        if not array:
            return None
        elif len(array) == 1:
            return TreeNode(array[0])

        n = len(array)
        head_node = TreeNode(array[n/2])
        left_child = self.create_bst(array[:n/2])
        right_child = self.create_bst(array[n/2 + 1:])
        
        head_node.left = left_child
        head_node.right = right_child

        return head_node

        
if __name__ == '__main__':
    unittest.main()

