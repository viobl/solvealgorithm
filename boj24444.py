from collections import deque
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)] # n까지 생성
ch = [0] * (n + 1)
cnt = 1 # 시작하는 정점 개수 카운팅

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(v):
    global cnt
    q = deque([r])
    ch[r] = 1

    while q:
        v = q.popleft()
        graph[v].sort()
        for g in graph[v]:
            if ch[g] == 0:
                cnt += 1
                ch[g] = cnt
                q.append(g)


BFS(r)
for v in ch[1:]:
    print(v)