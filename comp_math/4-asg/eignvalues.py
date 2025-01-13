import matrix_logic
import numpy as np

# matrix = [
#     [1, 2, 9],
#     [12, 11, 2],
#     [0, 0, 4]
# ]

n, m = int(input("number of rows: ")), int(input("number of col: "))
matrix = matrix_logic.matrix_init(n, m)

if len(matrix[0]) != len(matrix):
    matrix = [row[:-1] for row in matrix]

A = np.array(matrix, dtype=float)

eigenvalues = np.linalg.eigvals(A)

print("Numerical Eigenvalues:")
print(eigenvalues)

# example
# https://www.youtube.com/watch?v=gUe_aVtVThg