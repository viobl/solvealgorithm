import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0]

for x in a:
    if dp[-1] < x:
        dp.append(x)
    else:
        left = 0
        right = len(dp)

        while left < right:
            mid = (left + right) // 2
            if dp[mid] < x:
                left = mid + 1
            else:
                right = mid
        dp[right] = x

print(len(dp) - 1)


# for i in range(n):
#     start = 0
#     end = len(dp) - 1
#     print(end)
#
#     # 첫 턴 넘어감
#     while start <= end:
#         mid = (start + end) // 2
#         if dp[mid] < a[i]:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     if start >= len(dp):
#         dp.append(a[i])
#     else:
#         dp[start] = a[i]
#
# print(len(dp))