# 인구 이동
# 과정 이해는 됐다. 국가가 국경선을 여닫는 것을 확인 할 수 있는 방법??
# 인구이동이 며칠동안 일어나는지 소수점 버리고 이동 카운팅 필요
from collections import deque
import sys
input = sys.stdin.readline

graph = []
n, l, r = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    q = deque()
    tmp = []
    q.append((a, b))
    tmp.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 국경선 공유하는 두 나라의 인구 차 L~ R, 공유 국경선 하루 오픈
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    tmp.append((nx, ny))
    return tmp


res = 0
while 1:
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    flag = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                # 열려야하는 국경선이 모두 열리면, 인구 이동 시작
                if len(country) > 1:
                    flag = 1
                    # 연합을 이루고 있는 각 칸의 인구 - 소수점 버리기
                    number = sum([graph[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        graph[x][y] = number
    # 연합 해체, 모든 국경선 닫기
    if flag == 0:
        break
    res += 1

print(res)