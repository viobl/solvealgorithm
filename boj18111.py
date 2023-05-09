# 마인크레프트
# 보유 블록 수 내에서 install 가능
# install - uninstall 뭐가더 빠르고 적절한지 비교 제거는 2초, 설치는 1초
# 최소값을 저장해서 활용
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

res = 2147000000
idx = 0

# 0 ~ 256까지 반복
for x in range(257):
    maxS = 0
    minS = 0
    for i in range(n):
        for j in range(m):
            # 블록 >= 층
            if graph[i][j] >= x:
                maxS += graph[i][j] - x
            else: # 블록 < 층
                minS += x - graph[i][j]

    if maxS + b >= minS:
        # 최소 시간 비교
        if minS + (maxS * 2) <= res:
            res = minS + (maxS * 2) # 최소 시간
            idx = x # 층 수

print(res, idx)