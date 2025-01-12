import matplotlib.pyplot as plt
import math
def func(x):
    return math.exp(-x)

def f_iteration():
    err = 1e-5
    x0, c = 1, 0
    prev_x0 = 0

    iterations, roots = [], []

    while c == 0 or abs(x0-prev_x0) >= err:
        prev_x0 = x0
        # print("x{}: {}".format(c, func(x0)))
        roots.append(x0)
        iterations.append(c)
        x0 = func(x0)
        c+=1
    return iterations, roots

# plt.plot(iterations, roots, "r-",marker="o")
# plt.grid() 
# plt.xlabel("Iterations")
# plt.ylabel("X's roots")
# plt.show()
    