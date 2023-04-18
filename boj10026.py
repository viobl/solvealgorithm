# 적록 색약
# 구역 카운팅과 유사 빨, 파는 같은 색 취급/ 다른 취급 나눠서
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
board = [list(map(str, input().rstrip())) for _ in range(n)] # char div => rstrip
visited = [[False] * n for _ in range(n)]
c2Cnt, c3Cnt = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    visited[x][y] = True
    curColor = board[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            # 현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs
            if visited[nx][ny] == False:
                if board[nx][ny] == curColor:
                    DFS(nx, ny)


# 정상
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            DFS(i, j)
            c3Cnt += 1

# 색맹 R -> G
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            DFS(i, j)
            c2Cnt += 1

print(c3Cnt, c2Cnt)