# 섬나라의 섬 개수 세기
from collections import deque
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0 # 지나가면서 체크
            Q.append((i, j)) # 체크한 것들 일단 큐로
            while Q:
                tmp = Q.popleft() # 체크한 것 기준으로 추출해서 전개
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0 # 다시 초기화
                        Q.append((x, y))
            cnt += 1 # 초기화 한 것 마무리하며 카운팅
print(cnt)