# 소인수 분해 : 수 입력 되면 나눈 인수들 출력
n = int(input())

if n == 1:
    print('')

for i in range(2, n + 1):
    # 나누어 떨어지는 것 작은 것부터 체크
    if n % i == 0:
        # dfs 활용? 단순 반복문으로 해보자
        while n % i == 0:
            print(i)
            n = n / i

