# 우선 해당 데이터를 매트릭스에 넣는것
# n x n 행렬 1행 정중앙, 2행 정중앙 -1 ~ +1, ... , [n/2] + 1 행 풀, 이후 +1 행마다 양끝 -1 해서 적용
# 하면서 해당 성분들 모두 더한 값 결과로 출력
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)] * n
sum = 0
Q = deque()
ch[n // 2][n // 2] = 1
sum += a[n // 2][n // 2]
Q.append((n // 2, n // 2))
L = 0

while True:
    if L == n // 2:
        break

    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0: # 체크 했던건 합산 제외
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1

print(sum)