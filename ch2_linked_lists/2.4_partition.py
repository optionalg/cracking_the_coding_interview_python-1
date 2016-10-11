# [2.4] Partition: Write code to partition a linked list around
# a value x, such that all nodes less than x come before all
# nodes greater than or equal to x. If x is contained within
# the list, the values of x only need to be after the elements
# less than x (see below). The partition element x can appear
# anywhere in the "right partition"; it does not need to appear
# between left anr right partitions.

# EXAMPLE
# Input: 3, 5, 8, 5, 10, 2, 1 (partition = 5)
# Output: 3, 1, 2, 10, 5, 5, 8

# Space complexity: O(1)
# Time complexity: O(N)

import unittest

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition_list(node, partition):
    # keep track of four pointers to two groups
    # initialize less_than_start
    less_than_start = None
    # initialize less_than_end
    less_than_end = None
    # initialize greater_or_equal_start
    greater_or_equal_start = None
    # initialize greater_or_equal_end
    greater_or_equal_end = None

    # execute steps while entire list has not been traversed
    while node:
        # keep track of next node
        next = node.next
        # set current node to point to none
        node.next = None

        # if node value is less than partition
        if node.value < partition:
            # check if less_than_start exists
            if not less_than_start:
                # if it does not, set the node to be the start
                less_than_start = node
                # also set the node to be the end
                less_than_end = node
            # if less_than_start does exist
            else:
                # set less_than_end to point to this node
                less_than_end.next = node
                # set less_than_end to be that node
                less_than_end = node

        # if node is greater than or equal to partition
        else:
            # check if greater_or_equal_start exists
            if not greater_or_equal_start:
                # if it does not, set node to be the start
                greater_or_equal_start = node
                # also set node to be the end
                greater_or_equal_end = node
            # if it does 
            else:
                # set end to point to this node
                greater_or_equal_end.next = node
                # set end point to be this node
                greater_or_equal_end = node

        # set node to next
        node = next

    # if there is no less_than group
    if not less_than_start:
        # return greater_than_start
        return greater_or_equal_start

    # if there is a less_than group
        # make less_than_end point to greater start
        # return less_than start
    less_than_end.next = greater_or_equal_start
    return less_than_start

class Test(unittest.TestCase):
    alist1 = Node(1, Node(1, Node(1, Node(5, Node(1, Node(1, Node(1)))))))
    alist2 = Node(1, Node(1, Node(10, Node(5, Node(1, Node(1, Node(1)))))))

    def test_partition_list(self):
        result1 = partition_list(Test.alist1, 5)
        result2 = partition_list(Test.alist2, 5)

        self.assertEqual(self.node_vals_to_list(result1), [1,1,1,1,1,1,5])
        self.assertEqual(self.node_vals_to_list(result2), [1,1,1,1,1,10,5])

    def node_vals_to_list(self, node):
        result = []
        while node:
            result.append(node.value)
            node = node.next

        return result
        
if __name__ == '__main__':
    unittest.main()
