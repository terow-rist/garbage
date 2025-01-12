import sympy as sym 

n, m = int(input("number of rows: ")), int(input("number of col: "))

matrix = []
for i in range(0, n):
    print("Enter {}'s list.".format(i+1))
    if i == 0:
        print("Example: 1,2..n = [1, 2..n]")
    matrix.append([int(j) for j in input().split()])

should_be, c = len(matrix[0]), 1
for i in matrix:
    if len(i) != should_be or len(i) != m:
        print("length of the column {} is incorrect.".format(c))
        exit(1)
    should_be = len(i)
    c+=1



A = sym.Matrix(matrix)

print(A.rref(pivots=True))

# Example of 3x4 matrix
# 1 1 1 9
# 2 -3 4 13
# 3 4 5 40
