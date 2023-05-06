# 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)] # 직관적이해를 위해 0번 인덱스 비우면서 n개

for i in range(1, n): # 1~n-1 항까지 n개 입력, n-1로 해도 됨
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 무방향 그래프

visited = [0] * (n + 1)
def DFS(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            DFS(i)

DFS(1)
# 2번 노드부터 출력
for i in range(2, n + 1):
    print(visited[i])