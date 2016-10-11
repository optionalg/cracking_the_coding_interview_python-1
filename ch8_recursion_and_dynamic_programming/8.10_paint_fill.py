# [8.10] Paint Fill: Implement the "paint fill" function that 
# one might see on many image editing programs. That is, given
# a screen (represented by a two-dimensional array of colors),
# a point, and a new color, fill in the surrounding area until 
# the color changes from the original color.

import unittest

def paint_fill(grid, row, col, color):
    target_color = grid[row][col]
    paint_fill_helper(grid, row, col, target_color, color)
    
def paint_fill_helper(grid, row, col, color_from, color_to):
    if not coords_in_bounds(grid, row, col):
        return

    if grid[row][col] == color_from:
        grid[row][col] = color_to
        paint_fill_helper(grid, row-1, col, color_from, color_to)
        paint_fill_helper(grid, row+1, col, color_from, color_to)
        paint_fill_helper(grid, row, col-1, color_from, color_to)
        paint_fill_helper(grid, row, col+1, color_from, color_to)


def coords_in_bounds(grid, row, col):
    row_in_bounds = row < len(grid) and row >= 0
    col_in_bounds = col < len(grid[0]) and col >= 0
    return row_in_bounds and col_in_bounds

class Test(unittest.TestCase):
    def setUp(self):
        self.grid = [
            ['white', 'white','red','red'],
            ['white', 'white','white','white'],
            ['white', 'white','white','white'],
            ['blue', 'blue','white','white'],
            ['blue', 'blue','white','white'],
        ]
        self.result = [
            ['blue', 'blue','red','red'],
            ['blue', 'blue','blue','blue'],
            ['blue', 'blue','blue','blue'],
            ['blue', 'blue','blue','blue'],
            ['blue', 'blue','blue','blue'],
        ]

    
    def test_paint_fill(self):
        paint_fill(self.grid, 0, 0, 'blue')
        self.assertEqual(self.grid, self.result)


if __name__ == '__main__':
    unittest.main()

