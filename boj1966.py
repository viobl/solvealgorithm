from collections import deque
tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0

    while q:
        best = max(q)  # 최댓값이 판단의 기준
        front = q.popleft()
        m -= 1  # 궁금한 것 위치 한 칸 앞으로

        if best == front:
            cnt += 1  # 방출됨에 따라 순번 증가
            if m < 0:
                print(cnt) # 뭘 더 하려하지 말고 출력
                break

        else:
            q.append(front)
            if m < 0:  # 최전방에서 pop
                m = len(q) - 1  # 최후방으로