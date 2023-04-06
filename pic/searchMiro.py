# 최단거리를 DFS로 구현하기
def DFS(x, y):
    global cnt
    # 도착점
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4): # 상하좌우
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and miro[xx][yy] == 0:
                miro[xx][yy] = 1
                DFS(xx, yy)
                miro[xx][yy] = 0 # 거치고 난 후 초기화



miro = [list(map(int, input().split())) for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0 # 도착 경우 가지수
miro[0][0] = 1
DFS(0, 0)
print(cnt)