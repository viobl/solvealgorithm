# 단지 개수 세기랑 유사
from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(a, b):
    q = deque([])
    q.append((a, b)) # tuple save
    board[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                q.append((nx, ny))
                board[nx][ny] = 0

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    board = [[0] * (m) for _ in range(n)] # 가로세로 잘 따져보기 range(행의 개수, 세로 길이)
    cnt = 0
    for _ in range(k):
        a, b = map(int, input().split())
        board[a][b] = 1


    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)