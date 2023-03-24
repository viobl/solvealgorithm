# 소수
# 1줄~2줄 사이 범위의 소수들 체크하고, 해당소수의 합 첫줄 출력 & 두번째 줄 제일작은 소수 출력, 없으면 -1
m = int(input())
n = int(input())
prime =[]

for num in range(m, n + 1):
    check = 0
    # num이 소수인지 판별 후 리스트 추가
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                check += 1
                break # 멈춰야 연산 더 하지않고 끝냄
        if check == 0:
            prime.append(num)

# 소수 합 출력, 제일 작은 소수 출력
if len(prime) > 0 :
    print(sum(prime))
    print(min(prime))
else:
    print(-1)