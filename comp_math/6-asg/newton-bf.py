import math

def newton_forward_interpolation(x_values, y_values, x):
    n = len(x_values)
    h = x_values[1] - x_values[0]   
 
    diff_table = [[0 for _ in range(n)] for _ in range(n)]
 
    for i in range(n):
        diff_table[i][0] = y_values[i]
 
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = round(diff_table[i + 1][j - 1] - diff_table[i][j - 1], 5)

    print("Forward Difference Table:")
    for row in diff_table:
        print(row)
 
    u = (x - x_values[0]) / h
    interpolated_value = y_values[0]
    u_term = 1

    for i in range(1, n):
        u_term *= (u - (i - 1))
        interpolated_value += (u_term * diff_table[0][i]) / math.factorial(i)

    return interpolated_value

def newton_backward_interpolation(x_values, y_values, x):
    n = len(x_values)
    h = x_values[1] - x_values[0]

    diff_table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        diff_table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = round(diff_table[i + 1][j - 1] - diff_table[i][j - 1], 5)

    print("Backward Difference Table:")
    for row in diff_table:
        print(row)

    u = (x - x_values[-1]) / h
    interpolated_value = y_values[-1]
    u_term = 1

    for i in range(1, n):
        u_term *= (u + (i - 1))
        interpolated_value += (u_term * diff_table[n - i - 1][i]) / math.factorial(i)

    return interpolated_value

# Example data
data_x = [10, 20, 30, 40]
data_y = [1.1, 2.0 , 4.4, 7.9]
value_to_interpolate = 2.5

# Choose interpolation method based on proximity to the start or end of the dataset
if value_to_interpolate - data_x[0] < data_x[-1] - value_to_interpolate:
    result = newton_forward_interpolation(data_x, data_y, value_to_interpolate)
    print(f"Interpolated value at x = {value_to_interpolate} using Forward Interpolation is {result}")
else:
    result = newton_backward_interpolation(data_x, data_y, value_to_interpolate)
    print(f"Interpolated value at x = {value_to_interpolate} using Backward Interpolation is {result}")