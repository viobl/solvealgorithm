# 말처럼 움직이려는 원숭이
# 체스의 말처럼 이동 -> 전진 막혀있을 경우에 이동처리는 어떻게 하는가?
# k회 나이트처럼 이동, 그 외에 한 칸씩만
# 나이트처럼 이동 카운팅 if 이동 횟수 = k시 불가능 별도 함수 모듈로 관리해야하는가 => 일괄 처리 분기처리
# 이동방식이 일관되지 않을 경우 3차원 리스트에서 방문처리 하는 방식을 생각해볼 수 있다 <- 범위로 시간복잡도 힌트
from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hx = [2, 2, -2, -2, 1, 1, -1, -1]
hy = [1, -1, 1, -1, 2, -2, 2, -2]

# bfs 이동
def bfs():
    q = deque()
    q.append((0, 0, k))
    visited = [[[0 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
    while q:
        x, y, z = q.popleft()
        # 도착 시 리턴
        if x == h - 1 and y == w - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내, 방문하지 않은 지점 탐색
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))

        if z > 0:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 0 and visited[nx][ny][z - 1] == 0:
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
                    q.append((nx, ny, z - 1))
    return -1

print(bfs())