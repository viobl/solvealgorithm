# 변형된 n, m 인데 역시나... 비내림차순이랑 오름차순의 차이가 뭐지?
n, m = map(int, input().split())
s = []

def dfs(start):
    # 출력 시점
    if len(s) == m:
        print(' '.join(map(str, s)))
        return


    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)