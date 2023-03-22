# 정점 간선, 시작점 입력 첫줄
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # 런타임 에러 시간제한 풀기

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

def dfs(v):
    global count # 전역변수 설정
    visited[v] = count # 방문한 정점 카운팅
    graph[v].sort()

    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            dfs(g)

for i in range(m): # 간선 수 m개
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 시작점부터 dfs
dfs(r)

# 방문한 정점 출력
for i in range(1, n + 1):
    print(visited[i])