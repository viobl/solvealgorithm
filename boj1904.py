n = int(input())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746 # 백만단위로 int 범위를 넘어서기 때문에 문제에 제시된 수 이용
print(dp[n])