import matplotlib.pyplot as plt
import sympy as sym 
from sympy import *
n, m = int(input("number of rows: ")), int(input("number of col: "))
e = 1e-5

# matrix = [
#     [2, 1, 1, 6],
#     [1, 3, -1, 0],
#     [-1, 1, 2, 3]
# ]
matrix = []
# Input matrix logic
for i in range(0, n):
    print("Enter {}'s list.".format(i+1))
    if i == 0:
        print("Example: 1 2 ... n = [1, 2..n]")
    matrix.append([int(j) for j in input().split()])

should_be, c = len(matrix[0]), 1
for i in matrix:
    if len(i) != should_be or len(i) != m:
        print("length of the column {} is incorrect.".format(c))
        exit(1)
    should_be = len(i)
    c+=1

# Values of each Xi in matrix 
# Initialize symbols for sympy
x_list = [0]*len(matrix)
x_symbols = symbols('x1:'+str(len(matrix)+1))

# Create expression for each variable
c = 0
expressions = [] 
for i in matrix:
    expr = sum([coef*var for coef, var in zip(i, x_symbols)]) - i[-1]
    expressions.append(solve(expr, x_symbols[c])[0])
    # print(solve(expr, x_symbols[c]))
    c+=1

# Iteration proccess
c = 0
result, errors = [], []
converged = False
while not converged:
    new_x_list = []
    for exp in expressions:
        res = {x_symbols[i]: x_list[i] for i in range(len(matrix))}
        new_x_list.append(float(exp.subs(res)))
    
    converged = all(abs(new_x_list[i] - x_list[i]) < e for i in range(len(x_list)))
    errors.append([abs(new_x_list[i] - x_list[i]) for i in range(len(x_list))])
    result.append(x_list)
    x_list = new_x_list
    c+=1

# Start for plotting
transposed_result = list(zip(*result))  
err_result = list(zip(*errors))
iterations = [i for i in range(c)]

for i, values in enumerate(transposed_result):
    plt.plot(iterations, values, marker="o", label=f"x{i+1}")  

plt.title("Jacobi method.")
plt.grid()
plt.xlabel("Iterations")
plt.ylabel("X's Roots")
plt.legend()
plt.show()

for i, values in enumerate(err_result):
    plt.plot(iterations, values, marker="o", label=f"x{i+1}")  

plt.title("Errors of Jacobi method.")
plt.grid()
plt.xlabel("Iterations")
plt.ylabel("X's Roots")
plt.legend()
plt.show()

