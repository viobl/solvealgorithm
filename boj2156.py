# 포도주 최대로 마시기
# 이전에 계단오르기와 유사, but 최대값 필요
# dp, a의 인덱스 값을 일괄적으로 적용해서 혼동이 없을만한 방안?
import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)] # 보다 가독성이 좋은 코드는??
dp = [0] * n

dp[0] = a[0]
if n > 1:
    dp[1] = a[0] + a[1]

if n > 2:
    dp[2] = max(a[2] + a[1], a[2] + a[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 3] + a[i - 1] + a[i], dp[i - 2] + a[i])

print(dp[n - 1])