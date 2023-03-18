n, m = map(int, input().split())
basket = [n for n in range(1, n+1)]

# m번 교환
for _ in range(m):
    a, b = map(int, input().split())
    basket = basket[0 : a - 1] + basket[a - 1: b][::-1] + basket[b:]
    # a까지는 원래대로/ a~b까지는 역순/ b부터 원래대로

print(" ".join(str(s) for s in basket))
