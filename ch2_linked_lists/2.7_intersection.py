# [2.7] Intersection: Given two (singly) linked lists,
# determine if the two lists intersect. return the 
# intersecting node. Note that the intersection is 
# defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same 
# (by reference) as the jth node of the second linked
# list, then they are intersecting.

# Space complexity: O(1)
# Time complexity: O(n)

import unittest

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def get_intersecting_node(list1, list2):
    if not list1 or not list2:
        raise ValueError('Must include two linked lists')

    if lists_intersect(list1, list2):
        list1, list2 = make_same_length(list1, list2)
        while list1:
            if list1 == list2:
                return list1
            else:
                list1 = list1.next
                list2 = list2.next

    return None

def make_same_length(list1, list2):
    list1_length = get_list_length(list1)
    list2_length = get_list_length(list2)
    list_diff = abs(list1_length - list2_length)

    if list1_length < list2_length:
        longer_list = list2
        shorter_list = list1
    else:
        longer_list = list1
        shorter_list = list2

    for _ in xrange(list_diff):
        longer_list = longer_list.next

    return shorter_list, longer_list


def get_list_length(node):
    count = 0
    while node:
        node = node.next
        count += 1

    return count

def lists_intersect(list1, list2):
    if not list1 or not list2:
        return False

    while list1:
        list1_prev = list1
        list1 = list1.next

    while list2:
        list2_prev = list2
        list2 = list2.next

    if list1_prev == list2_prev:
        return True

    return False

class Test(unittest.TestCase):
    
    def test_lists_intersect(self):
        head1 = Node(5)
        head2 = Node(5)
        list_body = Node(1, Node(2, Node(3)))
        a_node = Node(5)
        list_body.next = a_node
        head1.next = list_body
        head2.next = a_node
        self.assertTrue(lists_intersect(head1, head2))

    def test_get_intersecting_node(self):
        head1 = Node(5)
        head2 = Node(5)
        list_body = Node(1, Node(2, Node(3)))
        a_node = Node(5)
        list_body.next = a_node
        head1.next = list_body
        head2.next = a_node
        self.assertEqual(get_intersecting_node(head1, head2), a_node)
        self.assertRaises(ValueError, get_intersecting_node, head1, None)

        
if __name__ == '__main__':
    unittest.main()

