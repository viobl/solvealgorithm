import sys
input = sys.stdin.readline

def DFS(x, y):
    # y값 변하지 않을때 중단
    if y == 1:
        return x % c

    # 계산 용이하도록 재귀
    tmp = DFS(x, y // 2)
    # x^y 꼴에서 지수 y 짝수일 때
    if y % 2 == 0:
        return tmp * tmp % c
    else:
        return tmp * tmp * x % c


a, b, c = map(int, input().split())
res = DFS(a, b)
print(res)