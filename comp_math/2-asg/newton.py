import matplotlib.pyplot as plt
import math
def func(x):
    return x-math.exp(-x)
def deriv_func(x):
    return 1+math.exp(-x)

def f_newton():
    err = 1e-5
    iterations, roots = [], []

    x0, prev_x0 = 1, 0
    c = 0
    while c == 0 or abs(x0-prev_x0) >= err:
        prev_x0 = x0
        # print("x{}: {}".format(c, x0))
        roots.append(x0)
        iterations.append(c)
        x0 = x0 - func(x0)/deriv_func(x0)
        c+=1
    return iterations, roots

# plt.plot(iterations, roots, "r-",marker="o")
# plt.grid() 
# plt.xlabel("Iterations")
# plt.ylabel("X's roots")
# plt.show()
    