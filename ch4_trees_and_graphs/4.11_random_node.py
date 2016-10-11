# [4.11] Random Node: You are implementing a binary tree
# class from scratch which in addition to insert, find,
# and delete, has a method getRandomNode() which returns
# a random node from the tree. All nodes should be
# equally likely to be chosen. Design and implement an
# algorithm for getRandomNode, and explain how you would
# implement the rest of the methods.

import unittest
from random import randint


class TreeNode(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.left_size = 0

    def insert(self, node):
        if node.value < self.value:
            if not self.left:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
            self.left_size += 1
        else:
            if not self.right:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def find_by_rank(self, rank):
        current_node_rank = self._get_rank()

        if current_node_rank == rank:
            return self
        elif rank < current_node_rank:
            return self.left.find_by_rank(rank)
        else:
            return self.right.find_by_rank(rank)

    def get_random_node(self):
        random_pos = self._generate_random_number()
        return self.find_by_rank(random_pos)

    def _get_rank(self):
        if not self.parent:
            return self.left_size
        elif self.parent.value > self.value:    
            return self.left_size
        else:
            return self.left_size + self.parent._get_rank() + 1

    def _get_highest_rank(self):
        if not self.right:
            return self._get_rank()
        else:
            return self.right._get_highest_rank()

    def _generate_random_number(self):
        return randint(0,_get_highest_rank())

class Test(unittest.TestCase):
    
    def setUp(self):
        self.binary_tree = TreeNode(7)
        self.n3 = TreeNode(3)
        self.n1 = TreeNode(1)
        self.n5 = TreeNode(5)
        self.n10 = TreeNode(10)
        self.n8 = TreeNode(8)
        self.n12 = TreeNode(12)

        self.binary_tree.insert(self.n3)
        self.binary_tree.insert(self.n1)
        self.binary_tree.insert(self.n5)
        self.binary_tree.insert(self.n10)
        self.binary_tree.insert(self.n8)
        self.binary_tree.insert(self.n12)

    def test_insert(self):
        self.assertEqual(self.binary_tree.left.value, 3)
        self.assertEqual(self.binary_tree.left.left.value, 1)
        self.assertEqual(self.binary_tree.left.right.value, 5)
        self.assertEqual(self.binary_tree.right.value, 10)
        self.assertEqual(self.binary_tree.right.left.value, 8)
        self.assertEqual(self.binary_tree.right.right.value, 12)

        self.assertEqual(self.binary_tree.left_size, 3)
        self.assertEqual(self.n3.left_size, 1)
        self.assertEqual(self.n10.left_size, 1)

    def test_get_rank(self):
        self.assertEqual(self.binary_tree._get_rank(), 3)
        self.assertEqual(self.n1._get_rank(), 0)
        self.assertEqual(self.n5._get_rank(), 2)
        self.assertEqual(self.n10._get_rank(), 5)
        self.assertEqual(self.n12._get_rank(), 6)

    def test_get_highest_rank(self):
        self.assertEqual(self.binary_tree._get_highest_rank(), 6)

    def test_find_by_rank(self):
        self.assertEqual(self.binary_tree.find_by_rank(3), self.binary_tree)
        self.assertEqual(self.binary_tree.find_by_rank(0), self.n1)
        self.assertEqual(self.binary_tree.find_by_rank(2), self.n5)
        self.assertEqual(self.binary_tree.find_by_rank(5), self.n10)

if __name__ == '__main__':
    unittest.main()

