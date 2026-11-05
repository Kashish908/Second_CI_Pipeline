def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    # Use list comprehension to swap rows and columns
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
