import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# dict - key, value로 판단? 단순 리스트로 sort?
# w, v
# burden = [list(map(int, input().split())) for _ in range(n)]
burden = [(0, 0)]
for _ in range(n):
    burden.append(list(map(int, input().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)] # dp[n][k]는 n번째까지 봤을때 최대 가치
for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = burden[i][0]
        v = burden[i][1]

        if j < w: # 무게가 더 크면 그 전 계산
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)


print(dp[n][k])