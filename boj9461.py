# p[n] = p[n - 2] + p[n - 3] 1~3 항 까지는 1로 제시
tc = int(input())
p = [0] * 102
p[0], p[1], p[2] = 1, 1, 1

for i in range(3, 101):
    p[i] = p[i - 2] + p[i - 3]
    # p[i].append(a)

for i in range(tc):
    a = int(input())
    print(p[a - 1])