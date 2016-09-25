#Time complexity: O(N**2)

import unittest

def rotate_matrix(matrix):
    #input is in list of lists 
    #matrix[row][col]

    N = len(matrix)
    layers = N/2
    
    #rotate by layers
    #if number of layers is odd, don't need to rotate last one
    for layer in xrange(layers):

        # don't do the last pos because the first move
        # puts the initial first value of the row in the last place
        # pos traverses between rows for top and bottom and cols for
        # left and right
        for pos in xrange(layer, N - layer - 1):
            
            #store the top value
            top = matrix[layer][pos]
            
            #override top value with left
            matrix[layer][pos] = matrix[N-pos-1][layer]
            
            #override left with bottom
            matrix[N-pos-1][layer] = matrix[N-layer-1][N-pos-1]
            
            #override bottom with right
            matrix[N-layer-1][N-pos-1] = matrix[pos][N-layer-1]
            
            #override right with stored top
            matrix[pos][N-layer-1] = top

    return matrix

class Test(unittest.TestCase):
    m1 = [[1,2],[3,4]]
    m1_rotated = [[3,1],[4,2]]

    m2 = [[1,2,3],[4,5,6],[7,8,9]]
    m2_rotated = [[7,4,1],[8,5,2],[9,6,3]]

    m3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    m3_rotated = [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]

    def test_rotate_matrix(self):
        self.assertEqual(rotate_matrix(Test.m1), Test.m1_rotated)
        self.assertEqual(rotate_matrix(Test.m2), Test.m2_rotated)
        self.assertEqual(rotate_matrix(Test.m3), Test.m3_rotated)

if __name__ == '__main__':
    unittest.main()