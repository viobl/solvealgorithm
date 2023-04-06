dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    # 도착점
    if x == ex and y == ey:
        cnt += 1
    else:
        for i in range(4): # 상하좌우
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0 # 거치고 난 후 초기화


n = int(input())
board = [[0] * n for _ in range(n)]
ch = [[0] * n for _ in range(n)]
max = -2147000000
min = 2147000000
for i in range(n):
    tmp = list(map(int, input().split()))
    # starting point search
    for j in range(7):
        if tmp[j] < min:
            min = tmp[j]
            sx = i
            sy = j
        if tmp[j] > max:
            max = tmp[j]
            ex = i
            ey = j
        board[i][j] = tmp[j]
    ch[sx][sy] = 1
    cnt = 0
    DFS(sx, sy)
    print(cnt)