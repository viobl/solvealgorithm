# 3색 칠하기
# 일직선 기준 해당 집의 좌우와는 색이 다르도록
# 각 줄의 1열 빨, 2열 초, 3열 파 색칠 비용
import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n): # 양 옆과 비교해서 최소인 것 색칠 + 해당 인덱스 색칠 값
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]

print(min(rgb[n - 1]))

