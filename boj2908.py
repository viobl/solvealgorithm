# 상수 2개 들어오는 것 거꾸로 읽고 비교하기
# 0포함 아닌 같지 않은 3자리

n1, n2 = input().split()
n1 = int(n1[::-1]) # 거꾸로 할때
n2 = int(n2[::-1])

if (n1 > n2):
    print(n1)
else :
    print(n2)