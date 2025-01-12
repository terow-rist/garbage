import false_position, iteration, newton, bisection
import matplotlib.pyplot as plt

def plot_bisection():
    iterations, roots = bisection.f_bisection()
    plt.plot(iterations, roots, "r-", marker="o", label="Bisection method")

def plot_iteration():
    iterations, roots = iteration.f_iteration()
    plt.plot(iterations, roots, "g-", marker="o", label="Iteration method")

def plot_false_position():
    iterations, roots = false_position.f_false_position()
    plt.plot(iterations, roots, "b-", marker="o", label="F.P. method")

def plot_newton():
    iterations, roots = newton.f_newton()
    plt.plot(iterations, roots, "y-", marker="o", label="N.R. method")



plot_bisection()
plot_false_position()
plot_iteration()
plot_newton()

plt.grid()
plt.xlabel("iterations")
plt.ylabel("X's roots")
plt.legend()
plt.show()