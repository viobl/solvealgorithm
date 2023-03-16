# 스도쿠
# 가로 1~9 있는지 확인
# 작은 정사각형 1~9 확인 <= 어떻게?
import sys
def checkRow(x, n):
    for i in range(9):
        if n == graph[x][i]:
            return False
    return True

def checkCol(y, n):
    for i in range(9):
        if n == graph[i][y]:
            return False
    return True

def checkRect(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == graph[nx + i][ny + j]:
                return False
    return True


def solution(n):
    # 빈 칸을 채움
    if n == len(blank):
        for _ in range(9):
            print(*graph[_])
        exit(0)

    # 1부터 9까지 넣어서 확인하기
    for i in range(1, 10):
        x = blank[n][0] # 빈 x좌표
        y = blank[n][1] # 빈 y좌표

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            solution(n + 1)
            graph[x][y] = 0


graph = []
blank = []
# 9x9 create
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        # check blank
        if graph[i][j] == 0:
            blank.append([i, j])

solution(0)
