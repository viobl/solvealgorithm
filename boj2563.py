# 색종이 : 색칠한 부분 넓이 구하기
# 전체 100x100 매트릭스 구현 후 해당 범위 인덱스 반복문 돌려서 0 바꾸기, 1로 바꾼 것 개수세기
m = [[0] * 100 for i in range(100)]
n = int(input())

for i in range(n):
    x, y = list(map(int, input().split()))

    for row in range(x, x + 10):
        for col in range(y, y + 10):
            m[row][col] = 1

res = 0
for i in m:
    res += i.count(1)

print(res)