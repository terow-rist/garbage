import math
import matplotlib.pyplot as plt 
# def func(x):
#     return x*math.exp(x)-1
def func(x):
    return x**3-x-1


def f_bisection():
    a, b = 1, 2
    err = 1e-10
    c = 0

    iterations, roots = [], []
    while abs(a-b) >= err:
        xi = (a+b)/2
        if func(xi)*func(b) < 0:
            a = xi 
        else:
            b = xi
        print("x{}: {}".format(c, xi))
        iterations.append(c)
        roots.append(xi)
        # delta_x.append(abs(a-b))
        c += 1
    return iterations, roots

f_bisection()

# plt.subplot(1, 2, 1)
# plt.plot(iterations, roots, "r-", marker="o")
# plt.grid()
# plt.xlabel("iterations")
# plt.ylabel("X's roots")

# plt.subplot(1, 2, 2)
# plt.plot(iterations, delta_x, marker="o")
# plt.grid()
# plt.xlabel("iterations")
# plt.ylabel("delta's X")
# plt.show()