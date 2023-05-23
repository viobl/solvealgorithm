# 다리만들기
# 1차 bfs로 영역 탐색
# 2차 다리 설치 과정 bfs하면서 카운팅, 최소 지점 스탑
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
num = 1
res = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1차 섬 영역 탐색
def bfs(i, j):
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = 1 # 방문 처리
                graph[nx][ny] = num
                q.append([nx, ny])


# 2차. 최단거리 탐색 저장
def buildBridge(v):
    queue = deque()
    distance = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == v:
                distance[i][j] = 0
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 다른 섬 만나서 연결했을 경우
                if graph[nx][ny] and graph[nx][ny] != v:
                    return distance[x][y]
                # 다리 설치 예상 경로
                elif (not graph[nx][ny]) and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append([nx, ny])

    return int(1e9)


# 섬 영역 구분
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            visited[i][j] = 1
            graph[i][j] = num
            bfs(i, j)
            num += 1

# 최단거리 구하기
for v in range(1, num):
    res = min(res, buildBridge(v))

print(res)