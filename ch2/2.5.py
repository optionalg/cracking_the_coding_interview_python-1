# [2.5] Sum Lists: You have two numbers represented by a linked
# list, where each node contains a single digit. The digits
# are stored in reverse order, such that the 1's digit is at 
# the head of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.

# FOLLOW UP
# Suppose the digits are stored in forward order.

# Example: (7, 1, 6) + (5, 9, 2) -> (2,1,9)

# Space complexity: O(N)
# Time complexity: O(N)

import unittest

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_lists_reverse(node1, node2):
    summed_list = add_lists(reverse_list(node1), reverse_list(node2))
    return reverse_list(summed_list)

def add_lists(node1, node2, carry_received=0):
    if check_if_no_values(node1, node2, carry_received):
        return None

    node_sum = add_nodes(node1, node2, carry_received)
    sum_node_value, carry_pass = split_carry_value(node_sum)
    remaining_list = get_remaining_list(node1, node2, carry_pass)
    current_node = Node(sum_node_value)
    current_node.next = remaining_list
    
    return current_node

def check_if_no_values(node1, node2, carry):
    if carry == 0:
        if not (node1 or node2):
            return True
    
    return False

def add_nodes(node1, node2, carry):
    if node1 and node2:
        node_sum = node1.value + node2.value + carry
    elif node1 or node2:
        remaining_node = node1 or node2
        node_sum = remaining_node.value + carry
    else:
        node_sum = carry

    return node_sum

def split_carry_value(node_sum):
    if node_sum >= 10:
        carry_pass = 1
        node_sum -= 10
    else:
        carry_pass = 0

    return node_sum, carry_pass
    
def get_remaining_list(node1, node2, carry_pass):
    if node1 and node2:
        remaining_list = add_lists(node1.next, node2.next, carry_pass)
    elif node1:
        remaining_list = add_lists(node1.next, None, carry_pass)
    elif node2:
        remaining_list = add_lists(None, node2.next, carry_pass) 
    else:
        remaining_list = add_lists(None, None, carry_pass)

    return remaining_list

def reverse_list(node, previous=None):
    while node:
        next = node.next
        node.next = previous
        previous = node
        node = next
    return previous


class Test(unittest.TestCase):
    
    def test_add_lists(self):
        list1a = Node(7, Node(1, Node(6)))
        list1b = Node(5, Node(9, Node(2)))
        list_sum1 = add_lists(list1a, list1b)
        self.assertEqual(self.node_vals_to_list(list_sum1), [2,1,9])

        list2a = Node(7, Node(1, Node(6)))
        list2b = Node(5, Node(9, Node(4)))
        list_sum2 = add_lists(list2a, list2b)
        self.assertEqual(self.node_vals_to_list(list_sum2), [2,1,1,1])

        list3a = Node(7)
        list3b = Node(3, Node(0, Node(1)))
        list_sum3 = add_lists(list3a, list3b)
        self.assertEqual(self.node_vals_to_list(list_sum3), [0,1,1])

    def test_reverse_list(self):
        list1 = reverse_list(Node(3, Node(0, Node(1))))
        self.assertEqual(self.node_vals_to_list(list1), [1, 0, 3])

        list2 = None
        self.assertEqual(self.node_vals_to_list(list2), None)

    def test_add_lists_reverse(self):
        list1a = Node(7, Node(1, Node(6)))
        list1b = Node(5, Node(9, Node(2)))
        list_sum1 = add_lists_reverse(list1a, list1b)
        self.assertEqual(self.node_vals_to_list(list_sum1), [1,3,0,8])

        list2a = Node(7, Node(1, Node(6)))
        list2b = Node(5, Node(9, Node(4)))
        list_sum2 = add_lists_reverse(list2a, list2b)
        self.assertEqual(self.node_vals_to_list(list_sum2), [1,3,1,0])

        list3a = Node(7)
        list3b = Node(3, Node(0, Node(1)))
        list_sum3 = add_lists_reverse(list3a, list3b)
        self.assertEqual(self.node_vals_to_list(list_sum3), [3,0,8])    

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
