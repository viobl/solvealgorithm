n, m = map(int, input().split())
# a = list(map(int, input().split()))

# 바구니별 할당 넘버링 리스트
basket = [i for i in range(1, n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    tmp = basket[b - 1] # tmp 하나 더 만들어서 3중 거래방식으로
    basket[b - 1] = basket[a - 1]
    basket[a - 1] = tmp
print(*basket) # 리스트 제거하고 나열