import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
# 물어본 것이 두 지점 사이의 최대 거리. 즉, 간격을 물어봄(다른 것은 상관 없다)
house.sort()
start = 1
end = house[-1] - house[0]
res = 0

while(start <= end):
    mid = (start + end) // 2
    cnt = 1
    current = house[0]
    gap = end

    # 현재 위치와의 차이 계산
    for i in range(1, n):
        # 기준보다 크면 공유기 설치 카운팅
        if house[i] - current >= mid:
            gap = min(gap, house[i] - current)
            cnt += 1
            current = house[i]

    if cnt >= c: # 설치 가능 => 증가
        start = mid + 1
        res = max(res, gap)

    else: # 설치 불가 => 감소
        end = mid - 1

print(res)