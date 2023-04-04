# 요세푸스 문제 : n까지 큐에서 k번째 반복해서 빼내는 것
from collections import deque
n, k = map(int, input().split())
dQ = deque()
for i in range(1, n + 1):
    dQ.append(i)


print('<', end='')

while dQ:
    for i in range(k - 1): # k번째 제외하고 pop 후에 최후방에서 append
        dQ.append(dQ[0])
        dQ.popleft()
    print(dQ.popleft(), end='')

    if dQ:
        print(', ', end='')

print('>')