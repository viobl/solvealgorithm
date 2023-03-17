n, m=map(int, input().split())
box = [0] * n # 빈 배열 만들기

for _ in range(m): # 개수대로
    i, j, k = map(int, input().split())

    for idx in range(i, j + 1):
        box[idx - 1] = k

for i in range(n):
    print(box[i], end = ' ')