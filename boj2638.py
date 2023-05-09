# 치즈 업그레이드
# 두변 이상 맞닿아 있을 경우 녹음 -> 두변을 어떻게 알아낼 것인가, 상하좌우 이동 확인하며 카운팅 but 치즈 내부는 아니어야함
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로 격자 수, 가로 격자수
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 추후 방문할 필요 없는 공기 표시
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                # 치즈가 있는 위치 구별을 위해 누적 표시
                elif graph[nx][ny] == 1:
                    visited[nx][ny] += 1

    # 2면 이상 접하고, 1시간 이후 녹아야할 것 별도 리스트를 통해 확인
    melted = []
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                melted.append((i, j))

    return melted

res = 0
while True:
    melted = bfs()

    if not melted:
        break
    res += 1
    for x, y in melted:
        graph[x][y] = 0

print(res)