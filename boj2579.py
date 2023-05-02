import sys
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]
dp = [0] * n

# 계단 마지막꺼 밟기 - 연속 3개ㄴㄴ
if len(s) <= 2: # 계단 2개 이하 전체 합
    print(sum(s))
# 계단 3개 이상
else:
    dp[0] = s[0]
    dp[1] = s[0]+s[1]
    for i in range(2, n): # 직전 계단 기준 이전 계단 o/x 최대값
        dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])

    print(dp[n - 1])