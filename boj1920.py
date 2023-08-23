import sys
input = sys.stdin.readline

# 딕셔너리
n = int(input())
nList = set(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

for i in mList:
    if i in nList:
        print("1")
    else:
        print("0")

# 이분탐색으로?
