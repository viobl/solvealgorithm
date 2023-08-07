import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
cnt = 0

for _ in range(n):
    s = input().rstrip()
    dict[s] = True

for _ in range(m):
    s = input().rstrip()
    if s in dict:
        cnt += 1

print(cnt)