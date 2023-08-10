import sys
input = sys.stdin.readline

n = int(input())
divisors = list(map(int, input().split()))

maxD = max(divisors)
minD = min(divisors)

print(maxD * minD)