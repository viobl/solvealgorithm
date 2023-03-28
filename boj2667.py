n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True

    return False

cnt = 0
res = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(cnt)
            res += 1
            cnt = 0

num.sort()
print(res)
for i in range(len(num)):
    print(num[i])