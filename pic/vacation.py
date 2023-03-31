# 휴가
def DFS(L, sum):
    global res
    if L == n + 1: # 종료되는 날짜
        if sum > res:
            res = sum
    else:
        if L + t[L] <= n + 1:
            DFS(L + t[L], sum + p[L])
        DFS(L + 1, sum)

n = int(input())
t = []
p = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 최소값 될만한 것 설정
res=-2147000000
t.insert(0, 0) # 인덱스를 1일차라고 보기위해 0번에는 0을 넣어서 미뤄버리기
p.insert(0, 0)
DFS(1, 0) # 1일차부터 시작
print(res)