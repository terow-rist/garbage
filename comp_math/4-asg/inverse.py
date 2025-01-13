import sympy as sym 
import matrix_logic
# matrix = [
#     [5, 2, 1, 7],
#     [-1, 4, 2, 3],
#     [2, -3, 10, -1]
# ]
n, m = int(input("number of rows: ")), int(input("number of col: "))
matrix = matrix_logic.matrix_init(n, m)

if len(matrix[0]) != len(matrix):
    matrix = [row[:-1] for row in matrix]

A = sym.Matrix(matrix)

inverse = A.inv()

new_mx = []
print("Inverse of the square matrix:")
for row in inverse.tolist():  # Convert the matrix to a list of lists
    print(row)
    new_mx.append([float(i) for i in row])

print("In terms of numercial values.")
for i in new_mx:
    print(i)