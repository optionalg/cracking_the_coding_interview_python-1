# [2.3] Delete Middle Node: Implement an algorithm to delete a 
# node in the middle (i.e., any node but the first and last
# node, not necessarily the exact middle) of a singly linked
# list, given only access to that node.

# Space complexity: O(1)
# Time complexity: O(N)

import unittest

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next
    
class Test(unittest.TestCase):

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    
    def test_delete_middle_node(self):
        delete_middle_node(Test.n3)
        self.assertEqual(self.node_vals_to_list(Test.n1),[1,2,4,5])

        delete_middle_node(Test.n2)
        self.assertEqual(self.node_vals_to_list(Test.n1),[1,4,5])

    def node_vals_to_list(self, node):
        result = []
        while node:
            result.append(node.value)
            node = node.next

        return result
        
if __name__ == '__main__':
    unittest.main()