# 전기줄 dp 연결 활용
# 기존의 것을 활용해서 어떻게 일괄적으로 처리 할 수 있을지를 고민
# 역방향으로 탄다고 다 걸리는 것이 아니네
n = int(input())
connect = [list(map(int, input().split())) for _ in range(n)]
dp = [1] * n

connect.sort()
for b in range(n):
    for a in range(b):
        if connect[a][1] < connect[b][1]:
            dp[b] = max(dp[b], dp[a] + 1) # B의 앞순서가 뒷순서보다 작을 때만 카운팅++

# 최대로 연결되는 수를 빼면, 제거해야하는 선 개수
print(n - max(dp))