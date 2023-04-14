# DFS 첫줄 BFS 둘째줄
from collections import deque
n, m, v = map(int, input().split())
board = [[0] * (n + 1) for _ in range(n + 1)]
ch1 = [0] * (n + 1) # 방문한 정점만 기록
ch2 = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1

def DFS(v):
    ch1[v] = 1
    print(v, end=' ')

    for i in range(1, n + 1):
        if ch1[i] == 0 and board[v][i] == 1: # 방문하지 않았지만, 간선은 있는 곳
            DFS(i)


def BFS(v):
    q = deque([v])
    ch2[v] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in range(1, n + 1):
            if ch2[i] == 0 and board[v][i] == 1: # check 한 것 안 한것 명확하기 로직 따라가면서 구분하기
                q.append(i)
                ch2[i] = 1


DFS(v)
print()
BFS(v)