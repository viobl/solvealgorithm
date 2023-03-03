# 동근 위치 기준
# 북or남 쪽 라인에 있을 때 : 동or서쪽 라인 가는 길이 + 해당 라인에서 거리 동부터면 그 위치대로, 서부터면 가로길이 - 위치
# 동서 쪽 라인에 있을때 : 동or서로 가는 길이 + 북or 남으로 의 거리
# 계속 다 변할때마다 두는게 맞나? => 아예 기준점을 잡고 절대값으로 거리만 계산하자 => 다 남쪽,
# 왼쪽, 상단 기준으로 좌표 설정해서 절대 거리, 근데 아무래도 기존 좌표평면과 달라 익숙하진 않네
import sys
w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
route = []
answer = 0

def getDistance(x, y):
    if x == 1:  # 북
        return y
    if x == 2:  # 남
        return w + h + w - y
    if x == 3:  # 서
        return w + h + w + h - y
    if x == 4:  # 동
        return w + y

for _ in range(n + 1):  # (0, 0)-상점 거리
    x, y = map(int, input().split())
    route.append(getDistance(x, y))

for i in range(n):  # 동근-상점 최단거리
    route1 = abs(route[-1] - route[i])
    route2 = 2 * (w + h) - route1
    answer += min(route1, route2)

print(answer)