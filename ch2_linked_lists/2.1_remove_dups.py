# [2.1] Write code to remove duplicates from an 
# unsorted linked list. What if a temporary buffer
# is not allowed?

# Hash table
# Space complexity: O(N)
# Time complexity: O(N)

# No buffer
# Space complexity: O(1)
# Time complexity: O(N^2)

import unittest

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def remove_dup_w_hash_table(node, previous=None):
    value_counter = {}
    first = node

    while node:
        if node.value in value_counter:
            previous.next = node.next
        else:
            value_counter[node.value] = 1
        previous = node
        node = node.next

    return first

def remove_dup_no_buffer(node):
    first = node
    current = node
    runner = node

    while current:
        previous = runner
        runner = runner.next

        if runner and runner.value == current.value:
            previous.next = runner.next
            runner = runner.next
        
        if runner is None:
            current = current.next
            runner = current

    return first

def convert_node_to_list(node):
    list_format = []
    while node:
        list_format.append(node.value)
        node = node.next
    return list_format

class Test(unittest.TestCase):
    
    def test_remove_up_no_buffer(self):
        linked_list1 = Node(1, Node(2, Node(3, Node(5, Node(2)))))
        remove_dup_no_buffer(linked_list1)
        self.assertEqual(convert_node_to_list(linked_list1),[1,2,3,5])

    def test_remove_dup_w_hash_table(self):
        linked_list2 = Node(1, Node(2, Node(3, Node(5, Node(2)))))
        remove_dup_w_hash_table(linked_list2)
        self.assertEqual(convert_node_to_list(linked_list2),[1,2,3,5])
        
if __name__ == '__main__':
    unittest.main()

