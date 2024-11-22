def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
result1 = get_matrix(6, 7, 8)
result2 = get_matrix(10, 11, 12)
result3 = get_matrix(13, 14, 15)
print(result1)
print(result2)
print(result3)