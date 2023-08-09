import sys
input = sys.stdin.readline

a = list(map(str, input().strip()))
b = list(map(str, input().strip()))
al, bl = len(a), len(b)
dp = [0] * bl # 하나를 기준으로 다른 하나를 판단

for i in range(al):
    cnt = 0
    for j in range(bl):
        if cnt < dp[j]:
            cnt = dp[j]

        elif a[i] == b[j]: # 순서같은 것 나올 때마다 카우누팅
            dp[j] = cnt + 1

# 전체 중에 가장 큰 것
print(max(dp))

# 바꿔서도 적용 가능
# dp1 = [0] * al
# for i in range(bl):
#     count = 0
#     for j in range(al):
#         if count < dp1[j]:
#             count = dp1[j]
#
#         elif a[i] == b[j]:
#             dp1[j] = count + 1
#
# print(max(dp1))