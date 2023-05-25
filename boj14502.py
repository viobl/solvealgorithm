# 연구소
# 바이러스가 퍼지지 않도록 벽 3개만 설치해서 번지는 것 최소화
# 최소화를 위한 조건 - 3개밖에 없기에 현재 있는 벽을 활용, 주변에 아무것이 없다면 막아야한다
# 변하는 것이 여러개라면 하나만 변하도록 하고 다른 것은 변동하지 않도록 통제
# 범위자체가 3~8로 그렇게 넓지는 않다 최대 2^64의 경우 일괄적으로 적용할만한 것을 기준으로.
# 바이러스가 bfs로 이동하며 퍼짐
# 벽 3개를 세우고, 해당 경우에 따른 바이러스를 퍼뜨린후 0으로 유지되는 값들만 카운팅
# 바이러스 퍼뜨리고 벽 세우는 것은 무의미
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n 세로길이 m 가로 길이
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
maxSafety = 0

# 최초 안전지대 개수
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1


# 바이러스 전파
def bfsVirus():
    visited = [[0] * m for _ in range(n)]
    global maxSafety
    safety = 0
    q = deque()
    # 바이러스 위치 표기, 전파를 위한 좌표 큐에 저장
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                visited[i][j] = 1
                q.append((i, j))

    while q:
        x, y = q.popleft()
        # 상하좌우 전파
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                # 범위 내에 전파되지 않았던 지점 기준, 안전지대의 개수 카운팅
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    safety += 1
                    q.append((nx, ny))

    maxSafety = max(maxSafety, cnt - safety)



# 백트래킹으로 벽 설치 3개 제한 탐색
def dfsWall(cnt):
    if cnt == 3:
        bfsVirus()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfsWall(cnt + 1) # dfs로 벽 재귀
                graph[i][j] = 0


dfsWall(0) # 설치 개수 0개부터 시작
print(maxSafety - 3)