import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sp = {}

# 반복문으로 다 '추가'하는 방식이 아닌 '설정'하는 방식으로 적용해야함
for _ in range(n):
    site, pw = input().split()
    sp[site] = pw

for _ in range(m):
    print(sp[input().rstrip()]) # 공백제거 하여 출력