import sys
input = sys.stdin.readline

def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L + 1) # 작업을 하고 되돌아온 것
                ch[i] = 0 # 돌아온 후 초기화

n, m = map(int, input().split())
res = [0] * n
ch = [0] * (n + 1)
cnt = 0
DFS(0)
print(cnt)