from collections import deque
# 현위치 x 기준// x-1, x+1, 2x로 이동 가능
def bfs(v):
    Q = deque([v])
    while Q:
        v = Q.popleft()
        if v == k:
            return line[v]

        for cntV in (v + 1, v - 1, 2 * v ):
            if 0 <= cntV < 100001 and not line[cntV]:
                line[cntV] = line[v] + 1
                Q.append(cntV)

n, k = map(int, input().split())
line = [0] * 100001 # 주어진 범위상에서의 최대값
print(bfs(n))