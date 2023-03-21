table = [list(map(int, input().split())) for _ in range(9)]

maxNum = 0
maxRow, maxCol = 0, 0
for row in range(9):
    for col in range(9):
        if maxNum <= table[row][col]:
            maxRow = row + 1
            maxCol = col + 1
            maxNum = table[row][col]

print(maxNum)
print(maxRow, maxCol)