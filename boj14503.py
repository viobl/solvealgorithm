import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r, c, d = map(int, input().split())

# d가 0,3,2,1 순서로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        d = (d + 3) % 4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                #청소 한 쪽이후 넘어가기
                flag = 1
                break

    if flag == 0: # 4방향 모두 완료
        if graph[r - dx[d]][c - dy[d]] == 1: #후진해서 벽에 부딪힐때
            print(cnt)
            break
        else:
            r, c = r - dx[d], c - dy[d]