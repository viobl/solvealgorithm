import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(v):
    global cnt
    # 방문 확인
    visited[v] = True
    answer[v] = cnt #
    graph[v].sort(reverse = True)

    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = [0] * (n + 1)
cnt = 1

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(r)

for val in answer[1:]: # 시작 정점 제외
    print(val)