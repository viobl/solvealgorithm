import sys
input = sys.stdin.readline

def DFS(x, y, k):
    global res
    visited = board[x][y]

    for i in range(x, x + k):
        for j in range(y, y + k):

            # 확인한 곳이 아닐 때
            if board[i][j] != visited:
                # 반복하며 탐색
                for l in range(3):
                    for m in range(3):
                        DFS(x + l * k // 3, y + m * k // 3, k // 3) # k대신 3 단위로 추가하는 것이 아닌 유동적으로 몫에따라 처리

                return # 중요하다....수가 달라진다... 되돌려야한다....

    # 카운팅
    if visited == -1:
        res[0] += 1
    elif visited == 0:
        res[1] += 1
    else:
        res[2] += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = [0, 0, 0]
DFS(0, 0, n)

print(res[0])
print(res[1])
print(res[2])