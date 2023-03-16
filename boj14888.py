# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것
# 브루트 포스, 백트래킹
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
calc = list(map(int, input().split())) # +, -, *, //

maximum = -1e9
minimum = 1e9

# dfs 판단근거
def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum

    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # 연산 방법 정의 : 연산순서 관계없이 앞에서부터
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide: # 나누기 차감, 정수 기준으로만 계산
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

dfs(1, num[0], calc[0], calc[1], calc[2], calc[3])
print(maximum)
print(minimum)