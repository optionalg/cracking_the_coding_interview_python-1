# [8.13] Stack of Boxes: You have a stack of boxes, with width 
# w, heights h, and depths d. The boxes cannot be rotated
# and can only be stacked on top of one another if each box
# in the stack is strictly larger than the box above it
# in in width, height, and depth. Implement a method to compute
# the height of the tallest possible stack. The height of a 
# stack is the sum of the heights of each box.

import unittest

def max_stack_height_helper(boxes):
    if len(boxes) == 1:
        return boxes[0].height

    current_box = boxes[0]
    stackable_boxes = get_stackable_boxes(current_box, boxes[1:])

    if stackable_boxes:
        current_height = current_box.height + max_stack_height_helper(stackable_boxes)
    else:
        current_height = current_box.height

    return max(current_height, max_stack_height_helper(boxes[1:]))

def max_stack_height(boxes):
    boxes.sort(key=lambda x: x.height, reverse=True)
    return max_stack_height_helper(boxes)


def get_stackable_boxes(box, boxes):
    for i, top_box in enumerate(boxes):
        if box.can_stack(top_box):
            return boxes[i:]
    return None

class Box(object):
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def can_stack(self, top_box):
        return (
            self.width > top_box.width and
            self.height > top_box.height and
            self.length > top_box.length
        )

    def __repr__(self):
        return 'Box(%s, %s, %s)' % (self.width, self.height, self.length)


class Test(unittest.TestCase):
    def setUp(self):
        b1 = Box(1,1,1)
        b2 = Box(2,2,2)
        b3 = Box(3,3,3)
        self.boxes1 = [b1,b2,b3]

        b4 = Box(1,1,1)
        b5 = Box(3,2,2)
        b6 = Box(3,3,3)
        self.boxes2 = [b4,b5,b6]

        b7 = Box(6,4,4)
        b8 = Box(7,5,5)
        b9 = Box(7,8,2)
        self.boxes3 = [b7,b8,b9]

        b10 = Box(5,5,5)
        self.boxes4 = [b10]

    
    def test_max_stack_height(self):
        self.assertEqual(max_stack_height(self.boxes1), 6)
        self.assertEqual(max_stack_height(self.boxes2), 4)
        self.assertEqual(max_stack_height(self.boxes3), 9)
        self.assertEqual(max_stack_height(self.boxes4), 5)


if __name__ == '__main__':
    unittest.main()

    

