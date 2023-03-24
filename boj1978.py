# 소수 찾기
# 첫줄 개수, 2줄 스플릿해야하는 수들
n = int(input())
numbers = list(map(int, input().split()))
prime = 0

for num in numbers:
    check = 0
    if num > 1:
        for i in range(2, num): # 소수 정의 2부터 n-1까지 다
            if num % i == 0: # 나머지 0 이면 나눠 떨어진 것
                check += 1

        if check == 0: # 걸리는 거 없으면 소수
            prime += 1

print(prime)