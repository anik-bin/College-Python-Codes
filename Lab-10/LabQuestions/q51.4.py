# Compute a matrix rank

import numpy as np

matrixA = np.array([[1, 2, 3, 23],
                       [4, 5, 6, 25],
                       [7, 8, 9, 28],
                       [10, 11, 12, 41]])

print("The Rank of a Matrix: ", np.linalg.matrix_rank(matrixA))