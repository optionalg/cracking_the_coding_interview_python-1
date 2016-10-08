# [4.12] Paths with Sum: You are given a binary tree in
# which each node contains an integer value (which might
# be positive or negative). Design an algorithm to count
# the number of paths that sum to a given value. The
# path does not need to start or end at the root or a
# leaf, but it must go downwards (traveling only from
# parent nodes to child nodes)

import unittest


def count_paths(root, target_sum):
    running_total_tracker = {}
    running_total = 0
    return count_paths_helper(
        root, 
        target_sum, 
        running_total_tracker, 
        running_total
    )

def count_paths_helper(node, target_sum, tracker, running_total):
    if not node:
        return 0

    matches = 0
    running_total += node.value

    if running_total == target_sum:
        matches += 1
    
    diff = running_total - target_sum
    if diff in tracker:
        matches += tracker[diff]

    if running_total in tracker:
        tracker[running_total] += 1
    else:
        tracker[running_total] = 1

    matches += count_paths_helper(node.left, target_sum, tracker, running_total)
    matches += count_paths_helper(node.right, target_sum, tracker, running_total)

    tracker[running_total] -= 1

    return matches

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Test(unittest.TestCase):
    
    def setUp(self):
        self.root = TreeNode(1)
        self.n1 = TreeNode(2)
        self.n2 = TreeNode(3)
        self.n3 = TreeNode(1)
        self.n4 = TreeNode(1)
        self.n5 = TreeNode(-1)

        self.root.left = self.n1
        self.root.right = self.n2
        self.n1.right = self.n3
        self.n2.right = self.n4
        self.n4.right = self.n5

    def test_count_paths(self):
        self.assertEqual(count_paths(self.root, 3), 4)
        self.n6 = TreeNode(3)
        self.n5.right = self.n6
        self.assertEqual(count_paths(self.root, 3), 6)
        
if __name__ == '__main__':
    unittest.main()

