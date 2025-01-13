def matrix_init(n, m):
    matrix = []
    # Input matrix logic
    for i in range(0, n):
        print("Enter {}'s list.".format(i+1))
        if i == 0:
            print("Example: 1 2 ... n = [1, 2..n]")
        matrix.append([int(j) for j in input().split()])

    should_be, c = len(matrix[0]), 1
    for i in matrix:
        if len(i) != should_be or len(i) != m:
            print("length of the column {} is incorrect.".format(c))
            exit(1)
        should_be = len(i)
        c+=1
    return matrix

# matrix = []
# # Input matrix logic
# for i in range(0, n):
#     print("Enter {}'s list.".format(i+1))
#     if i == 0:
#         print("Example: 1 2 ... n = [1, 2..n]")
#     matrix.append([int(j) for j in input().split()])

# should_be, c = len(matrix[0]), 1
# for i in matrix:
#     if len(i) != should_be or len(i) != m:
#         print("length of the column {} is incorrect.".format(c))
#         exit(1)
#     should_be = len(i)
#     c+=1