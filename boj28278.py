import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    l = list(map(int, input().split()))

    if l[0] == 1:
        stack.append(l[1])

    elif l[0] == 2:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)

    elif l[0] == 3:
        print(len(stack))

    elif l[0] == 4:
        if len(stack):
            print(0)
        else:
            print(1)

    else:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)