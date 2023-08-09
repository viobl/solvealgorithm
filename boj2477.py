# 참외밭 계산
# 큰 직사각형에서 작은 직사각형을 빼는 방식?
# 방향 받은 것 기준으로 판단해서 계산하기? => 오답
import sys
input = sys.stdin.readline

k = int(input())
ds = [list(map(int, input().split())) for _ in range(6)]

# 반복문 돌리기 전에 초기화 하고 시작
width, wi = 0, 0
height, hi = 0, 0

for i in range(len(ds)):
    if ds[i][0] == 1 or ds[i][0] == 2:
        if width < ds[i][1]:
            width = ds[i][1]
            wi = i #
    elif ds[i][0] == 3 or ds[i][0] == 4:
        if height < ds[i][1]:
            height = ds[i][1]
            hi = i #

# 작은 사각형 계산
sWidth = abs(ds[(wi - 1) % 6][1] - ds[(wi + 1) % 6][1])
sHeight = abs(ds[(hi - 1) % 6][1] - ds[(hi + 1) % 6][1])

result = ((width * height) - (sWidth * sHeight)) * k
print(result)