import math
import rules

# 1. Trapezoidal rule for integral from (0 to 1) x³ dx (n=5)
def func1(x): 
    return x**3
print(f"1. Trapezoidal (0 to 1) x³ dx: {rules.trapezoid(func1, 0, 1, 5):.6f}")


# 2. Simpson's 1/3 rule
def func2(x): 
    return math.sin(x)
def func3(x): 
    return math.sqrt(abs(math.cos(x)))  # Added abs to prevent math domain errors

print("\n2. Simpson's 1/3:")
print(f"2.1 integral from (0 to π) sin(x) dx (n=10): {rules.simpson_1_3(func2, 0, math.pi, 10):.6f}")
print(f"2.2 integral from (0 to π/2) sqrt(cos(x)) dx (n=8): {rules.simpson_1_3(func3, 0, math.pi/2, 8):.6f}")

# 3. Simpson's 3/8 rule
def func4(x): 
    return 1 / (1 + x**3)

print("\n3. Simpson's 3/8:")
print(f"3.1 integral from (0 to 9) dx / (1 + x³) (n=9): {rules.simpson_3_8(func4, 0, 9, 9):.6f}")
print(f"3.2 integral from (0 to π/2) sin(x) dx (n=6): {rules.simpson_3_8(func2, 0, math.pi/2, 6):.6f}")

# 4. Evaluating integral from (0 to 1) dx / (1 + x)
def func5(x): 
    return 1 / (1 + x)

print("\n4. integral from (0 to 1) dx / (1 + x):")
print(f"4.1 Trapezoidal: {rules.trapezoid(func5, 0, 1, 6):.6f}")
print(f"4.2 Simpson's 1/3: {rules.simpson_1_3(func5, 0, 1, 6):.6f}")
print(f"4.3 Simpson's 3/8: {rules.simpson_3_8(func5, 0, 1, 6):.6f}")
