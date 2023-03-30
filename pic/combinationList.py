# 조합 구하기
import sys
def DFS(L, s): # Level
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        cnt += 1
        print()
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, i + 1) # 가지 기준으로 +



n, m = map(int, input().split())
res = [0] * (n + 1)
cnt = 0
DFS(0, 1)
print(cnt)