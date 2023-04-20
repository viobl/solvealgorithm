# 동적 프로그래밍
n = int(input())

def recur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return recur(n - 1) + recur(n - 2)

def dynamic(n):
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    cnt = 0
    for i in range(3, n + 1):
        cnt += 1
        dp[i] = dp[i - 1] + dp[i - 2]
    return cnt

print(recur(n), dynamic(n))