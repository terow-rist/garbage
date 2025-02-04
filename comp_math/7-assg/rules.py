# Trapezoidal Rule
def trapezoid(f, a, b, n):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return total * h

def simpson_1_3(f, a, b, n):
    if n % 2 != 0:
        n += 1  # Ensure n is even
    h = (b - a) / n
    total = f(a) + f(b)
    
    for i in range(1, n, 2):
        total += 4 * f(a + i * h)
    for i in range(2, n, 2):
        total += 2 * f(a + i * h)
    
    return (h / 3) * total

# Simpson's 3/8 Rule
def simpson_3_8(f, a, b, n):
    if n % 3 != 0:
        n += 3 - (n % 3)  # Ensure n is a multiple of 3
    h = (b - a) / n
    total = f(a) + f(b)
    
    for i in range(1, n):
        weight = 3 if i % 3 != 0 else 2
        total += weight * f(a + i * h)
    
    return (3 * h / 8) * total