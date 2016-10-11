# [4.3] List of Depths: Given a binary tree, design
# an algorithm which creates a linked list of all
# the nodes at each depth (e.g., if you have a tree
# with depth D, you'll have D linked lists)

import unittest


def create_lists_per_level(node, depth, levels=[]):
    if not node:
        return

    if depth == 0:
        levels.append(Node(node.value))
    else:
        if depth >= len(levels):
            levels.append(Node(node.value))
        else:
            level = levels[depth]
            while level:
                previous = level
                level = level.next

            previous.next = Node(node.value)

    create_lists_per_level(node.left, depth+1, levels)
    create_lists_per_level(node.right, depth+1, levels)

    return levels


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Test(unittest.TestCase):
    
    def test_create_lists_per_level(self):
        bst = self.create_bst(range(2,8))
        lists = create_lists_per_level(bst, 0)
        self.assertEqual(len(lists), 3)
        self.assertEqual(lists[0].value, 5)
        self.assertEqual(lists[1].value, 3)
        self.assertEqual(lists[1].next.value, 7)
        self.assertEqual(lists[2].value, 2)
        self.assertEqual(lists[2].next.value, 4)
        self.assertEqual(lists[2].next.next.value, 6)

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

    def node_vals_to_list(self, node):
        if node:
            result = []
            while node:
                result.append(node.value)
                node = node.next

            return result
        else:
            return None
        
if __name__ == '__main__':
    unittest.main()

