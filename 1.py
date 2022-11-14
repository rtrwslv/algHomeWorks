matrix = [[0,1,1,1], [1,1,1,1], [0,1,1,1]]
#matrix = [[1,0,1], [1,1,0], [1,1,0]]
result = 0

for i in range(len(matrix)):
    result += matrix[i].count(1)
for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        if matrix[i][j] == 1 and matrix[i][j + 1] == 1:
            if matrix[i + 1][j] and matrix[i + 1][j + 1]:
                result += 1
for i in range(len(matrix) - 2):
    for j in range(len(matrix[i]) - 2):
        if matrix[i][j] == 1 and matrix[i][j + 1] == 1:
            if matrix[i][j + 2] == 1:
                if matrix[i + 1][j] == 1 and matrix[i + 2][j] == 1:
                    if matrix[i + 1][j + 1] == 1 and matrix[i + 1][j + 2] == 1:
                        if matrix[i + 2][j + 1] == 1 and matrix[i + 2][j + 2] == 1:
                            result += 1
print(result)
