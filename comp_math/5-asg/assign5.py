import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Input Data
X_data = np.array([1.0, 2.5, 3.2, 4.1, 5.0, 6.3])
Y_data = np.array([2.1, 3.8, 6.0, 8.5, 11.3, 15.2])


# Models
def parabola(x, a, b, c):  # y = a*x^2 + b*x + c
    return a * x**2 + b * x + c

def line(x, a, b):  # y = a + b*x
    return a + b * x

def exponential(x, a, b):  # y = a*exp(b*x)
    return a * np.exp(b * x)

def ax_bx2(x, a, b):  # y = a*x + b*x^2
    return a * x + b * x**2

def ax_bOverx(x, a, b):  # y = a*x + b/x
    return a * x + b / x

# Fit and RMSE calculation
models = {
    "Parabola: y = a*x^2 + b*x + c": (parabola, [1, 1, 1]),
    "Linear: y = a + b*x": (line, [1, 1]),
    "Exponential: y = a*exp(b*x)": (exponential, [1, 0.1]),
    "ax + bx^2": (ax_bx2, [1, 1]),
    "a*x + b/x": (ax_bOverx, [1, 1])
}

rmse_values = []
fitted_curves = {}

for name, (func, p0) in models.items():
    try:
        if func == ax_bOverx:  # Handle division by zero
            X_nz = X_data[X_data != 0]
            Y_nz = Y_data[X_data != 0]
            params, _ = curve_fit(func, X_nz, Y_nz, p0=p0)
            Y_fit = np.full_like(X_data, np.nan)
            Y_fit[X_data != 0] = func(X_data[X_data != 0], *params)
        else:
            params, _ = curve_fit(func, X_data, Y_data, p0=p0)
            Y_fit = func(X_data, *params)
        
        rmse = np.sqrt(np.mean((Y_data - Y_fit) ** 2))
        rmse_values.append(rmse)
        fitted_curves[name] = (params, rmse, func)
    except RuntimeError:
        rmse_values.append(np.inf)
        fitted_curves[name] = (None, np.inf, func)

# Best model
best_model_name = min(fitted_curves, key=lambda name: fitted_curves[name][1])
best_params, best_rmse, best_func = fitted_curves[best_model_name]

print(f"Best model: {best_model_name} (RMSE = {best_rmse:.4f})")

# Plot best model
X_fit = np.linspace(min(X_data), max(X_data), 200)
Y_fit_best = best_func(X_fit, *best_params) if best_func != ax_bOverx else np.full_like(X_fit, np.nan)
if best_func == ax_bOverx:
    Y_fit_best[X_fit != 0] = best_func(X_fit[X_fit != 0], *best_params)

plt.figure(figsize=(8, 5))
plt.scatter(X_data, Y_data, color='red', label='Data')
plt.plot(X_fit, Y_fit_best, color='blue', label=f"{best_model_name}")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Best Fit Model')
plt.legend()
plt.grid(True)
plt.show()
