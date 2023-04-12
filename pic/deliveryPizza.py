# 페업의 기준을 무엇으로 삼을지
# 거리를 계산할때 가장 가까운 지점을 무엇으로 잡고 측정할지
def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
            sum += dis
        if sum < res:
            res = sum

    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L + 1, i + 1)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
hs = []
pz = []
cb = [0] * m # combination save pizza shop
res = 2147000000
for i in range(n):
    for j in range(n):
        if board[i][j] == 1: # 집 check
            hs.append((i, j))
        elif board[i][j] == 2: # 피자집 찾았을 경우
            pz.append((i, j))

DFS(0, 0)
print(res)