def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L + 1, sum + pv[L], time + pt[L])
        DFS(L + 1, sum, time)


n, m = map(int, input().split())
pv = []
pt = []

for i in range(n):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)

res = 0
DFS(0, 0, 0)
print(res)