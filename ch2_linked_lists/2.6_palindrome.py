# [2.6] Palindrome: Implement a function to check if
# a linked list is a palindrome.

# Time Complexity: O(N)
# Space Complexity: O(N)

import unittest

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_is_palindrome(node):
    if not node:
        raise ValueError("Must enter a list")

    list_copy = copy_list(node)
    list_reversed = reverse_list(node)
    
    list_length = get_length(node)
    
    for i in xrange(list_length/2 + 1):
        if list_reversed.value != list_copy.value:
            return False

        list_copy = list_copy.next
        list_reversed = list_reversed.next

    return True

def reverse_list(node, previous=None):
    while node:
        next = node.next
        node.next = previous
        previous = node
        node = next
    return previous

def copy_list(node):
    new_list = None

    while node:
        if new_list:
            new_list.next = Node(node.value)
            new_list = new_list.next
        else:
            new_list = Node(node.value)
            new_list_head = new_list
        node = node.next

    return new_list_head

def get_length(node):
    count = 0
    while node:
        count += 1
        node = node.next
    return count

class Test(unittest.TestCase):

    def test_copy_list(self):
        list1 = copy_list(Node(1, Node(4, Node(5, Node(4, Node(1))))))
        self.assertEqual(self.node_vals_to_list(list1), [1,4,5,4,1])

    
    def test_list_is_palindrome(self):
        list1 = Node(1, Node(4, Node(5, Node(4, Node(1)))))
        self.assertTrue(list_is_palindrome(list1))

        list2 = Node(1, Node(4, Node(5, Node(4))))
        self.assertFalse(list_is_palindrome(list2))

        list3 = None
        self.assertRaises(ValueError, list_is_palindrome, list3)

    def test_get_length(self):
        list1 = Node(1, Node(4, Node(5, Node(4))))
        self.assertEqual(get_length(list1), 4)

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
