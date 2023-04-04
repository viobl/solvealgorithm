# +1, -1, +5 순으로 돌아갈때 최초로 해당 지점에 도달하는 순간 체크
from collections import deque

n, m = map(int, input().split())
max = 10000
ch = [0] * (max + 1)
dis = [0] * (max + 1)
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= max:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[m])