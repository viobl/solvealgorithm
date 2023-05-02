# 원형큐의 원리 적용한 케이스
# popleft pop활용, append 적용 여부 다름
from collections import deque

n, m = map(int, input().split())
idx = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])

# 완전탐색으로 찾아야할지, 다른 계산 방법이 뭐있을까
# 큐 전체 길이에서 가장 가까운 값 절대값으로 인덱싱해서 찾기? -> 남은 길이 기준으로 시계 방향, 역방향 판단
cnt = 0
for i in idx:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q) // 2:
                q.rotate(-1)
                cnt += 1
            else:
                q.rotate(1)
                cnt += 1

print(cnt)