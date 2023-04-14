import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
# 나이트 이동 방식
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def BFS(x, y):
    Q = deque()
    Q.append([x, y])
    board[x][y] = 1
    while Q:
        a, b = Q.popleft()
        if a == gx and b == gy:
            print(board[gx][gy] - 1)
            return
        for j in range(8):
            xx = a + dx[j]
            yy = b + dy[j]
            if 0 <= xx < i and 0 <= yy < i and board[xx][yy] == 0:
                Q.append([xx, yy])
                board[xx][yy] = board[a][b] + 1


for _ in range(t):
    i = int(input()) # 체스판 한 변 길이
    # 현재 위치
    x, y = map(int, input().split())
    # 이동 해야할 위치
    gx, gy = map(int, input().split())
    board = [[0] * i for _ in range(i)]

    BFS(x, y)