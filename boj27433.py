# 팩토리얼 구현 - 재귀
# 0! = 1
n = int(input())

def dfs(x):
    if x > 0:
        return x * dfs(x - 1)
    else:
        return 1

print(dfs(n))