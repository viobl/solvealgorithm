# 순열 자체는 완전탐색 해야한다. n!
# 규칙성을 찾아서 구현해야한다. - 파스칼 삼각형(이항계수) 곱해서 더하기
import sys
def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end = ' ')
        sys.exit(0) # 사전순으로 제일 앞에 것만 출력하고 종료를 위해

    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0

n, f = map(int, input().split())
p = [0] * n
b = [1] * n
ch = [0] * (n + 1)

for i in range(1, n): # n번째는 어차피 1
    b[i] = b[i - 1] * (n - i) // i # / 하나만 하면 소수점계산 됨

DFS(0, 0)