odd_cnt = 0
even_cnt = 0
num = list(map(int, input("숫자 10개를 공백으로 구분하여 입력: ").split()))

for i in range(10):
    if num[i] % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print("홀수의 개수:", odd_cnt)
print("짝수의 개수:", even_cnt)