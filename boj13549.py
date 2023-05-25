# 숨바꼭질
# 위치 좌표 x 기준, 찾는 사람이 걸을 때 x-1 or x+1 1초소요
# 순간이동 할때  2*x 이동시 무시가능한 정도로 0초 소요
import sys
from collections import deque
input = sys.stdin.readline
q = deque()

n, k = map(int, input().split())
line = [0] * 100001

# q에 시작 지점부터
q.append(n)
line[n] = 1
while q:
    target = q.popleft()
    if target == k:
        print(line[k] - 1)

    for x in (2 * target, target + 1, target - 1):
        if 0 <= x < 100001 and line[x] == 0: # 방문하지 않았던 지점확인
            # teleport의 효용도가 좋아서 우선
            if x == 2 * target:
                line[x] = line[target]
                q.appendleft(x) # 우선순위로
            else:
                line[x] = line[target] + 1 # 시간을 더해주는 셈
                q.append(x)