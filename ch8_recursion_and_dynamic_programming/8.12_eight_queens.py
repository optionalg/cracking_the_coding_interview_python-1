# [8.12] Eight Queens: Write an algorithm to print all ways of
# arranging eight queens on an 8x8 chess board so that none
# of them share the same row, column, or diagonal. In this case,
# "diagonal" means all diagonals, not just the two that bisect
# the board.

import unittest

def queens(num_queens):
    results = []
    grid_size = num_queens
    columns = [None]*num_queens
    n_ways(columns, 0, results, grid_size)
    return results


def n_ways(columns, row, results, grid_size):
    
    if row == grid_size:
        results.append(columns)
        return

    for col in range(0, grid_size):
        if is_valid(columns, row, col, grid_size):
            cols_copy = columns[:]
            cols_copy[row] = col
            n_ways(cols_copy, row+1, results, grid_size)


def is_valid(columns, row1, col1, grid_size):
    
    if col1 in columns:
        return False

    for row2, col2 in enumerate(columns):
        if col2 is not None:
            if abs(col1 - col2) == abs(row1 - row2):
                return False

    return True


class Test(unittest.TestCase):
    
    def test_queens(self):
        self.assertEqual(len(queens(8)), 92)

if __name__ == '__main__':
    unittest.main()

