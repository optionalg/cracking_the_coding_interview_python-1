# [2.8] Loop Detection: Given a circular linked list, implement
# an algorithm that returns the node at the beginning of the
# loop.

# Space complexity: O(1)
# Time complexity: O(n)

import unittest

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def get_start_loop_node(node):
    first = node
    slow = node
    fast = node

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            loop_start_node = find_intersection(slow, first)
            return loop_start_node

    return None

def find_intersection(node1, node2):
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next

    return node1

class Test(unittest.TestCase):
    
    def test_get_start_loop_node(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        self.assertEqual(get_start_loop_node(n1), None)
        
        n5.next = n3
        self.assertEqual(get_start_loop_node(n1), n3)
        
if __name__ == '__main__':
    unittest.main()

