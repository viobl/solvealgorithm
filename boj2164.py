from collections import deque as dq

N = int(input())
dq = dq([i for i in range(1, N + 1)])

while (len(dq) > 1):
    dq.popleft()
    moveNum = dq.popleft()
    dq.append(moveNum)

print(dq[0])