# 길 있는 상황에서 미로 최단거리 길 카운팅하기
# bfs이용해서 트리 타고 최단만 체크하기?
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
Q = deque()

def BFS(x, y):
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1:
                board[xx][yy] = board[x][y]+1
                Q.append((xx, yy))

    # 마지막 값에서 카운트 값 뽑기
    return board[n - 1][m - 1]

print(BFS(0,0))