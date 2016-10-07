# [4.9] BST Sequences: A binary search tree was created by
# traversing through an array from left to right and 
# inserting each element. Given a binary search tree with
# distinct elements, print all possible arrays that could
# have led to this tree

# Time complexity: 
# The weave function looks like O(2^N). The bst_seq 
# recursively calls itself on a smaller subsegment.
# This might be duplicative for each node, so O(N^2)?
# This needs more thought, but looks like O(N^2*2^N)

import pprint
import unittest

class Node(object):
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

def weave(arr1, arr2, prefix, result):
    if not arr1 or not arr2:
        result.append(prefix + arr1 + arr2)
        return result

    h1 = arr1.pop(0)
    prefix += [h1]
    weave(arr1, arr2, prefix, result)
    arr1.insert(0, h1)
    prefix.pop()

    h2 = arr2.pop(0)
    prefix += [h2]
    weave(arr1, arr2, prefix, result)
    arr2.insert(0, h2)
    prefix.pop()

    return result

def bst_seq(node):
    if not node:
        return []
    
    if not node.left and not node.right:
        return [[node.value]]

    bst_result = []
    left = bst_seq(node.left)
    right = bst_seq(node.right)

    if left and right:
        for left_seq in left:
            for right_seq in right:
                suffix = weave(left_seq, right_seq, [], [])
                bst_result += [[node.value] + seq for seq in suffix]
    else:
        remaining = left or right
        for seq in remaining:
            suffix = weave(seq, [], [], [])
            bst_result += [[node.value] + a_seq for a_seq in suffix]

    return bst_result

class Test(unittest.TestCase):
    
    def test_bst_seq(self):
        root = Node(value=4)
        n2 = Node(value=2)
        n6 = Node(value=6)
        n5 = Node(value=5)
        n7 = Node(value=7)

        root.left = n2
        root.right = n6
        n6.left = n5
        n6.right = n7

        self.assertEqual(len(bst_seq(root)), 8)

if __name__ == "__main__":
    unittest.main()