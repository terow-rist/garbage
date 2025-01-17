import matrix_logic
import matplotlib.pyplot as plt
import sympy as sym 
from sympy import *

n, m = int(input("number of rows: ")), int(input("number of col: "))
e = 1e-5

# matrix = [
#     [5, 2, 1, 7],
#     [-1, 4, 2, 3],
#     [2, -3, 10, -1]
# ]
matrix = matrix_logic.matrix_init(n, m)

# Initial values of each Xi in the matrix
x_list = [-2.4, 5.0, 1]  # Initial guesses

# Initialize symbols for sympy
x_symbols = symbols('x1:'+str(len(matrix)+1))

# Create expression for each variable
c = 0
expressions = [] 
for i in matrix:
    expr = sum([coef * var for coef, var in zip(i[:-1], x_symbols)]) - i[-1]
    expressions.append(solve(expr, x_symbols[c])[0])
    c += 1

# Iteration process
c = 0
result, errors = [], []
converged = False
while not converged:
    new_x_list = x_list[:]
    for j, exp in enumerate(expressions):
        res = {x_symbols[k]: new_x_list[k] for k in range(len(matrix))}  # Use updated values
        new_x_list[j] = float(exp.subs(res))

    converged = all(abs(new_x_list[i] - x_list[i]) < e for i in range(len(x_list)))
    errors.append([abs(new_x_list[i] - x_list[i]) for i in range(len(x_list))])
    result.append(x_list)
    x_list = new_x_list
    c += 1

# Start for plotting
transposed_result = list(zip(*result))  
err_result = list(zip(*errors))
iterations = [i for i in range(c)]

for i, values in enumerate(transposed_result):
    plt.plot(iterations, values, marker="o", label=f"x{i+1}")  

plt.title("Gauss-Seidel Method")
plt.grid()
plt.xlabel("Iterations")
plt.ylabel("X's Roots")
plt.legend()
plt.show()

for i, values in enumerate(err_result):
    plt.plot(iterations, values, marker="o", label=f"x{i+1}")  

plt.title("Errors of Gauss-Seidel Method")
plt.grid()
plt.xlabel("Iterations")
plt.ylabel("Errors")
plt.legend()
plt.show()
