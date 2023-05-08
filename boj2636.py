# 치즈 녹는 속도
# BFS 활용 공기와 직접 접촉한 부분 1시간 후에 녹아서 사라짐
# 표면과 치즈 내부의 공기를 어떻게 구분할까
# 모두 사라질 때까지 걸리는 시간
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cheeze = []


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    cnt = 0 # 시간 경과 카운팅
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    # 치즈가 아닌 부분만 큐로
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    # 표면만 처리, 내부 공기와 접촉한 칸은 큐에 넣지 않음
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    cheeze.append(cnt)
    return cnt


time = 0
while 1:
    time += 1
    visited = [[0] * m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break

print(time - 1)
print(cheeze[-2])