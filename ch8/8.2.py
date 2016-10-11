# [8.2] Robot in a Grid: Imagine a robot sitting on the upper
# left corner of grid with r rows and c columns. The robot can
# only move in two directions, right and down, but certain
# cells are "off limits" such that the robot cannot step on
# them. Design an algorithm to find a path for the robot from
# the top left to the bottom right.


import unittest

def find_exit(maze):
    failed = {}
    return find_exit_helper(maze, failed, len(maze)-1, len(maze[0])-1)

def find_exit_helper(maze, failed, r, c):
    # coordinates have already been evaluated to not work
    if (r,c) in failed:
        return failed[(r,c)]

    # coordinates fail if they are out of bounds of the maze
    if r < 0 or c < 0:
        failed[(r,c)] = False
        return False

    # coordinates fail if there is a blocking pattern
    if maze[r][c] == 1:
        failed[(r,c)] = False
        return False

    # if the robot reaches coordinate 0,0 return that coordinate
    if r == 0 and c == 0:
        return [(r,c)]

    # recursively call on space above and to the left
    result = find_exit_helper(maze, failed, r-1, c) or find_exit_helper(maze, failed, r, c-1)
    
    # if robot eventually gets to coord 0,0 the path will be returned
    # otherwise will evaluate to False
    if result:
        return result + [(r,c)]
    else:
        return result

class Test(unittest.TestCase):
    
    def setUp(self):
        self.maze = [
            [0,0,0,0,0,0],
            [1,0,0,0,1,1],
            [1,1,0,0,1,1],
            [1,1,1,0,0,0],
            [1,1,0,1,1,0]
        ]

        self.maze2 = [
            [0,0,0,0,0,0],
            [1,0,0,0,1,1],
            [1,1,0,0,1,1],
            [1,1,1,1,0,0],
            [1,1,0,1,1,0]
        ]

    def test_find_exit(self):
        self.assertTrue(isinstance(find_exit(self.maze),list))
        self.assertFalse(isinstance(find_exit(self.maze2),list))
        

if __name__ == '__main__':
    unittest.main()

