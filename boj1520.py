# 등산로와 유사한 문제, 내림차순으로 현 좌표의 수보다 작은 구역으로 이동. 이동 불가시 롤백
# DFS인데 다 탐색하기 힘들다. 중복 되는 연산은 제외하기
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def DFS(sx, sy):
    # 종점 도착
    if sx == m - 1 and sy == n - 1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[sx][sy] != -1:
        return dp[sx][sy]

    ways = 0
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[sx][sy] > graph[nx][ny]:
            ways += DFS(nx, ny)

    dp[sx][sy] = ways
    return dp[sx][sy]


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(DFS(0, 0))
