import sys

input = sys.stdin.readline


def dfs(depth, idx):
    global minDiff
    if depth == n // 2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                # start team
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                # link team
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        # 절댓값 최소 갱신
        minDiff = min(minDiff, abs(power1 - power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)  # 찍고 dfs 메서드 돌고 오기
            visited[i] = False  # 갱신


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
minDiff = int(1e9)

dfs(0, 0)
print(minDiff)
