matrix = [list(map(int, input().split())) for _ in range(9)]

maximum_element = 0
row, col = 1, 1

for i in range(9):
    for j in range(9):
        if matrix[i][j] > maximum_element:
            maximum_element = matrix[i][j]
            row, col = i + 1, j + 1

print(maximum_element)
print(row , col)