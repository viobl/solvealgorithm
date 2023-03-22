# 연립1차 방정식 만족하는 해가 x, y 유일하게 존재
# 하나씩 다 하고 맞는거 확인
a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
            print(i, j)
