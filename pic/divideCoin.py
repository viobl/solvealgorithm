# 세명이 서로 다르게 합 따져서 코인 배분하기
# 제일 큰 사람 - 작은 사람 최소 차이 되도록, 3~12 동전 수
def DFS(L):
    global res
    if L == n:
        gap = max(money) - min(money)
        if gap < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = gap

    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L] # 상태트리 더해준 이후에 다시 빼줘야 다음 쪽으로 할 수 있다.

n = int(input())
coin = []
money = [0] * 3
res = 2147000000
for i in range(n):
    coin.append(int(input()))
DFS(0)
print(res)