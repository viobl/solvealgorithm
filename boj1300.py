import sys
input = sys.stdin.readline
# 어떻게 해서 k번째 수를 이분 탐색으로 푸는 지 알아둬야할 필요.
n = int(input())
k = int(input())
start = 1
end = k

while (start <= end):
    mid = (start + end) // 2
    cnt = 0

    for i in range(1, n + 1):
        cnt += min(mid // i, n)

    if cnt >= k:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)