# [5.8] Draw Line: a monochrome screen is stored as a single
# array of bytes allowing eight consecutive pixels to be stored
# in one byte. The screen has width w, where w is divisible by
# 8 (that is, no byte will be split across rows). The height
# of the screen, of course, can be derived from the length of the
# array and the width. Implement a function that draws a 
# horizontal line from (x1, y) to (x2, y).

# The method signature should look something like:
# drawLine(byte[] screen, int width, int x1, int x2, int y)

import unittest

def draw_line(screen, width, x1, x2, y):
    index_start = y*width + x1
    line_width = x2 - x1 + 1
    for i in xrange(line_width):
        screen[index_start + i] = 255

class Test(unittest.TestCase):

    def setUp(self):
        self.screen = []
        self.blank_byte = 0
        self.filled_byte = 255
        self.width = 3
        self.height = 4

        for i in xrange(self.width * self.height):
            self.screen.append(self.blank_byte)
    
    def test_draw_line(self):
        draw_line(
            screen = self.screen,
            width = self.width,
            x1 = 1,
            x2 = 2,
            y = 1
        )
        result = [self.blank_byte]*4 + [self.filled_byte]*2 + [self.blank_byte]*6
        self.assertEqual(self.screen,result)

if __name__ == '__main__':
    unittest.main()

