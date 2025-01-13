import sympy as sym
import matrix_logic

# Define the rectangular matrix
# matrix = [
#     [5, 2, 1, 7],
#     [-1, 4, 2, 3],
#     [2, -3, 10, -1]
# ]

n, m = int(input("number of rows: ")), int(input("number of col: "))
matrix = matrix_logic.matrix_init(n, m)

if len(matrix[0]) != len(matrix):
    square_matrix = [row[:-1] for row in matrix]

A = sym.Matrix(matrix)

determinant = A.det()

print(f"Determinant of the square matrix: {determinant}")
