import unittest

def set_zeros2(matrix):
    #Time Complexity: O(MN)
    #Space Complexity: O(1)
    if not matrix:
        raise Exception("Matrix is empty")

    rows = len(matrix)
    cols = len(matrix[0])

    first_row_zero = False
    first_col_zero = False

    # check if zero is in first row
    if 0 in matrix[0]:
        first_row_zero = True

    # check if zero is in first column
    for row in matrix:
        if row[0] == 0:
            first_col_zero = True
            break

    for row_index in xrange(1,rows):
        for col_index in xrange(1, cols):
            # use the first row and the first col
            # to tell us if that row or column should
            # be set to zero
            if matrix[row_index][col_index] == 0:
                matrix[0][col_index] = 0
                matrix[row_index][0] = 0

    # go through each row
    for row_index in xrange(1, rows):
        #check if the first item of each row is zero
        if matrix[row_index][0] == 0:
            #if it is, set each item in that row to 0
            for col_index in xrange(1, cols):
                matrix[row_index][col_index] = 0

    # go through each column
    for col_index in xrange(1, cols):
        # check if first item in col is zero
        if matrix[0][col_index] == 0:
            # if it is, set each item in col to 0
            for row_index in xrange(1, rows):
                matrix[row_index][col_index] = 0

    # if first row was flagged to be zero set
    # all items in it to 0
    if first_row_zero:
        for col_index in xrange(0,cols):
            matrix[0][col_index] = 0

    # if first col was flagged to be zero set
    # all items in it to 0
    if first_col_zero:
        for row_index in xrange(0,rows):
            matrix[row_index][0] = 0

    return matrix

class Test(unittest.TestCase):
    m1 = [
        [0,1,1],
        [1,1,1],
        [1,1,1]
    ]
    m1_after = [
        [0,0,0],
        [0,1,1],
        [0,1,1]
    ]

    m2 = [
        [0,1,1,1],
        [1,1,1,1],
        [1,1,1,0]
    ]
    m2_after = [
        [0,0,0,0],
        [0,1,1,0],
        [0,0,0,0]
    ]

    m3 = [
        [1,1,1,1],
        [1,1,0,1],
        [1,1,1,1]
    ]
    m3_after = [
        [1,1,0,1],
        [0,0,0,0],
        [1,1,0,1]
    ]

    def test_set_zeros2(self):
        self.assertEqual(set_zeros2(Test.m1),Test.m1_after)
        self.assertEqual(set_zeros2(Test.m2),Test.m2_after)
        self.assertEqual(set_zeros2(Test.m3),Test.m3_after)

if __name__ == '__main__':
    unittest.main()