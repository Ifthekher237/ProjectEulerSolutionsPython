# pascals triagle
row = 15
col = 15

triangle_matrix = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    for j in range(col):
        if i == 0 or j == 0:
            triangle_matrix[i][j] = 1

for i in range(1,row):
    for j in range(1, col):
        triangle_matrix[i][j] = triangle_matrix[i - 1][j] + triangle_matrix[i][j - 1]
"""
for i in range(row):
    for j in range(col):
        print(triangle_matrix[i][j], end = " ")
    print()

print()
"""
j = col -1
sum = 0
for i in range(row):
    sum += triangle_matrix[i][j]
    print(triangle_matrix[i][j], end = " ")
    j -= 1
print()
print(sum)


