a = int(input())
b = int(input())
c = int(input())

res = list(str(a * b * c))

for i in range(0, 10):
    cnt = 0
    for num in res:
        if i == int(num):
            cnt += 1
    print(cnt)  ## 추가 후 for문에 프린트해야 의미있다.