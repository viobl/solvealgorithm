# 안전지역
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = []
res = 1
maxNum = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    low = list(map(int, input().split()))
    graph.append(low)

    for j in low:
        if j > maxNum:
            maxNum = j


def dfs(x, y, num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if graph[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx, ny, num)


for i in range(maxNum):
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for x in range(n):
        for y in range(n):
            if graph[x][y] > i and visited[x][y] == 0:
                cnt += 1
                visited[x][y] = 1
                dfs(x, y, i)
    res = max(res, cnt)

print(res)