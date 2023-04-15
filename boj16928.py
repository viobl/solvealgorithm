# 뱀과 사다리 게임
# 최소 횟수로 올라가려면??
# 이동 칸이 가장 큰 것을 이용해야함, 해당 지점 도달을 위해 숏컷 활용 필요
from collections import deque
import sys

def bfs(v):
    Q = deque([v])
    ch[v] = 1
    while Q:
        target = Q.popleft()
        for i in range(1, 7):
            dice = target + i

            if dice > 100:
                continue

            cnt = route[dice]
            # 탐색하지 않은 칸 확인
            if ch[cnt] == 0:
                Q.append(cnt)
                ch[cnt] = ch[target] + 1
                if cnt == 100:
                    return


n, m = map(int, input().split())

# 사다리, 뱀인 경우에 이동 후 좌표로 기록
route = [i for i in range(101)]
for _ in range(n + m):
    sx, gx = map(int, input().split())
    route[sx] = gx

# 도달 위치에 따른 주사위 던진 횟수 체크
ch = [0] * 101

bfs(1)

# 100번째 칸까지 주사위 던진 횟수에서 1번 칸에서 카운트한 주사위 던진 횟수를 빼준다.
print(ch[100] - 1)