import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# 연속하는 두수 합의 최대만 출력
for i in range(1, n):
    a[i] = max(a[i], a[i - 1] + a[i]) # 기존 모든 연속 숫자합의 최대값과의 비교

print(max(a))