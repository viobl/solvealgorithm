import sys

while True:
    a, b = list(map(int, sys.stdin.readline().split()))
    if a == 0 and b == 0:
        break

    if a < b and b % a == 0:
        print("factor")
    elif a > b and a % b == 0:
        print("multiple")
    else:
        print("neither")