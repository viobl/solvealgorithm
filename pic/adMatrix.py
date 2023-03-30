# 인접 행렬
n, m = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m): # 행 개수의 범위만큼
    x, y, z = (map(int, input().split()))
    a[x][y] = z

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(a[i][j], end = ' ')
    print()