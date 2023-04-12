from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split()) # 해당 변수가 의미하는 것 정확한 확인
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()
dis = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))

# 1 익은 토마토, 0 익지 않은 토마토, -1 빈 공간
# 4방향 인접하는 모든 지점 토마토 익기 시작하고 빈공간은 막힌상태로
while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0: # 익지 않은 토마토 확인 필요, 범위설정 주의
            board[nx][ny] = 1
            dis[nx][ny] = dis[x][y] + 1
            Q.append((nx, ny))

flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0

result = 0
if flag == 1: # flag = 0 발견되지 않았을때
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)