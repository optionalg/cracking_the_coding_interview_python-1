# [4.8] First Common Ancestor: Design an algorithm and write
# code to find the first common ancestor of two nodes in
# a binary search tree. Avoid storing additional nodes in
# a data structure. NOTE: This is not necessarily a binary
# search tree.

import unittest


def find_first_common_ancestor(n1, n2, root):
    # find node where nodes are on left and right side
    n1_on_left = node_in_tree(n1, root.left)
    n2_on_left = node_in_tree(n2, root.left)

    if n1_on_left ^ n2_on_left:
        return root
    else:
        if n1_on_left:
            return find_first_common_ancestor(n1, n2, root.left)
        else:
            return find_first_common_ancestor(n1, n2, root.right)

def node_in_tree(target, node):
    if not node:
        return False

    if target == node:
        return True
    else:
        return (
            node_in_tree(target, node.left) or node_in_tree(target, node.right)
        )

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Test(unittest.TestCase):
    
    def setUp(self):
        self.n1 = TreeNode(1)
        self.n2 = TreeNode(2)
        self.n3 = TreeNode(3)
        self.n4 = TreeNode(4)
        self.n5 = TreeNode(5)
        self.n6 = TreeNode(6)

        self.n1.left = self.n2
        self.n1.right = self.n3
        self.n2.left = self.n4
        self.n2.right = self.n5
        self.n3.left = self.n6

    #@unittest.skip("skip for now")
    def test_find_first_common_ancestor(self):
        self.assertEqual(
            find_first_common_ancestor(self.n4, self.n5, self.n1),
            self.n2
        )
        self.assertEqual(
            find_first_common_ancestor(self.n4, self.n6, self.n1),
            self.n1
        )

    def test_node_in_tree(self):
        self.assertTrue(node_in_tree(self.n4, self.n2))
        self.assertTrue(node_in_tree(self.n3, self.n1))
        self.assertFalse(node_in_tree(self.n6, self.n2))
        
if __name__ == '__main__':
    unittest.main()

