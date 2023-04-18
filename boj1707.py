# 이분 그래프 두가지 색으로 지도 색칠하기랑 비슷한 개념
# 해당 테스트의 첫 줄에 입력되는 간선의 개수만큼 해당 행 입력 가능
from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())
def bfs(vs, group):
    Q = deque()
    Q.append(vs)
    if visited[vs] == 0:
        visited[vs] = 1  # grouping 1, 2// 아직 방문하지 않은 곳 0
    while Q:
        v = Q.popleft()

        color = visited[v]
        for i in graph[v]:  # 연결 된 모든 정점 확인
            if visited[i] == 0:
                Q.append(i)
                if color == 1:  # 현재의 정점과 다른 색상으로 색칠
                    visited[i] = 2
                else:
                    visited[i] = 1

            elif visited[i] == 1:
                if color == 1:
                    print("NO")
                    return False
            elif visited[i] == 2:
                if color == 2:
                    print("NO")
                    return False
    return True


for _ in range(tc):
    flag = 0
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v + 1): # 비연결그래프는 모든 정점 탐색 필요
        if not bfs(i, graph):
            flag = 1
            break
    if flag == 0:
        print("YES")