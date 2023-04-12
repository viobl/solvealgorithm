# 사다리 탈때 위에서 내려올때는 좌우 확인후 내려오기, 올라갈때는 좌우 확인후 올라가서 역산
# 특수값을 같는 매트릭스의 인덱스로 부터 행 -1하며 좌우확인 이동, or 위로 이동
# 이후 더이상 위로 갈 수 없을때 해당 인덱스 출력
def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y - 1 >= 0 and board[x][y - 1] == 1 and ch[x][y - 1] == 0:
            DFS(x, y - 1)
        elif y + 1 < 10 and board[x][y + 1] == 1 and ch[x][y + 1] == 0:
            DFS(x, y + 1)
        else:
            DFS(x - 1, y)


board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0] * 10 for _ in range(10)]

for y in range(10):
    if board[9][y] == 2: # 마지막 줄에서 지점 조회
        DFS(9, y)