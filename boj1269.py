import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split())) # set에 바로 입력 가능
b = set(map(int, input().split()))

print(len(a - b) + len(b - a))