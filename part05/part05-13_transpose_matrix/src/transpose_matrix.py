# Write your solution here
def transpose(matrix: list):
    matrix_copy = [row.copy() for row in matrix]
    i = 0
    while i in range(len(matrix)):
        j = 0
        while j in range(len(matrix[i])):
            matrix[i][j] = matrix_copy[j][i]
            j += 1
        i += 1
