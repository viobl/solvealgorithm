# 최소 동전으로 거스름돈 리턴
# 정지 시점, 아닌 것부터 범주를 좁혀가면서 처리
def DFS(L, sum):
    global res
    if L >= res:
        return
    if sum > res:
        return

    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L + 1, sum + a[i])


n = int(input())
a = list(map(int, input().split()))
m = int(input())
res = 2147000000

a.sort(reverse=True)
DFS(0, 0)
print(res)

