# 큰 것부터 차감해나가는 방식으로해서 멈추기 vs 작은 것부터 쌓아가는 방식으로 멈추기?
def DFS(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(cn[L] + 1):
            DFS(L + 1, sum + (cv[L] * i))


t = int(input())
k = int(input())
cv = []
cn = []
for i in range(k):
    p, n = map(int, input().strip().split())
    cv.append(p)
    cn.append(n)

cnt = 0
DFS(0, 0)
print(cnt)