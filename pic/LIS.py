# 최대부분 증가수열
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0) # 0번 idx 비우고 1번부터 시작하기위해
dy = [0] * (n + 1)
dy[1] = 1
res = 0

for i in range(2, n + 1):
    max = 0
    for j in range(i - 1, i, -1): # i-1부터 역순으로 하나씩
        if arr[i] > arr[j] and dy[j] > max: # 증가 수열 최대값 최신화
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]

print(res)