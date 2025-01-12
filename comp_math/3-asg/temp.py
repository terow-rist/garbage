import sympy as sym 
from sympy import *

# x_list = []
# for i in range(4):
#     x_list.append(symbols('x'+str(i+1)))
#     expr += 2*x_list[i]
# print(expr, type(expr))
matrix = [0]*8
x_symbols = symbols('x1:'+str(len(matrix)))
print(x_symbols)

print(sum([i*x for i, x in zip([i for i in range(10)], x_symbols)])+1)