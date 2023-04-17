from collections import deque
# import sys
# input = sys.stdin.readline
def BFS(sx, sy, drill, ch, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 뚫고 이동하는게 가능하고, 도달하지 못하면 -1 출력
    Q = deque()
    Q.append((sx, sy, drill))
    ch[sx][sy][drill] = 1

    while Q:
        cx, cy, drill = Q.popleft()
        if cx == row - 1 and cy == col - 1:
            return ch[cx][cy][drill]

        for i in range(4):
            xx = cx + dx[i]
            yy = cy + dy[i]
            if xx <= -1 or yy <= -1 or xx >= row or yy >= col:
                continue
            # 벽 뚫지 않았을 때
            if board[xx][yy] == 0 and ch[xx][yy][drill] == 0:
                Q.append((xx, yy, drill))
                ch[xx][yy][drill] = ch[cx][cy][drill] + 1

            # 벽 뚫었을 때
            if board[xx][yy] == 1 and drill == 0:
                Q.append((xx, yy, drill + 1))
                ch[xx][yy][drill + 1] = ch[cx][cy][drill] + 1
    return -1


row, col = map(int, input().split())
board = [list(map(int, input())) for _ in range(row)]
ch = [[[0] * 2 for _ in range(col)] for _ in range(row)] # 벽 1개 뚫을 때까지 적용하기 위해 3차원 배열 사용

print(BFS(0, 0, 0, ch, board))