import matplotlib.pyplot as plt
import math
def f(x):
    return  x**2-2*x-5

def f_false_position():
    a, b = 1, 0
    err = 1e-5
    iterations, roots = [], []
    c = 0
    prevxi, xi = 0, (a*f(b)-b*f(a))/(f(b)-f(a))
    while c == 0 or abs(prevxi-xi) >= err:
        if f(xi) * f(b) < 0:
            a = xi 
        else:
            b = xi 
        print("x{}: {}".format(c, xi))
        iterations.append(c)
        roots.append(xi)
        prevxi = xi
        xi = (a*f(b)-b*f(a))/(f(b)-f(a))
        c += 1  
    return iterations, roots

iterations, roots = f_false_position()

plt.plot(iterations, roots, "r-",marker="o")
plt.grid() 
plt.xlabel("iterations")
plt.ylabel("X's roots")
plt.show()
    