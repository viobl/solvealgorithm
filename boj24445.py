from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)
cnt = 1

# 방문 순서를 출력. 시작점이 1, 차례대로 읽어가는 순서에 따라 순위 결정. 끝에 도달하면 다시 읽어나가는 순서에 따라 출력
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
        graph[v].sort(reverse=True)
        for g in graph[v]:
            if ch[g] == 0:
                cnt += 1
                ch[g] = cnt
                q.append(g)


BFS(r)
for v in ch[1:]:
    print(v)