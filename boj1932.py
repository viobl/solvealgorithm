# 해당 줄까지 합 다 더하기
# 무조건 다 더해야할까, 특정 조건이 없는지 확인해야할 필요 있다.
import sys
input = sys.stdin.readline

n = int(input())
tri = []
k = 2
for _ in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(k):
        if j == 0: # 첫번째 누적
            tri[i][j] = tri[i][j] + tri[i - 1][j]
        elif i == j: # 마지막 누적
            tri[i][j] = tri[i][j] + tri[i - 1][j - 1]
        else: # 사이 항들 중 큰 것 기준 누적
            tri[i][j] = tri[i][j] + max(tri[i - 1][j - 1], tri[i - 1][j])
    k += 1

print(max(tri[n - 1]))