import sys
input = sys.stdin.readline

n = int(input())
attend = {}

# 이름, 출입 확인
# dictionary의 key, value를 list의 index, value처럼 활용
for _ in range(n):
    a, b = map(str, input().split())

    if b == 'enter':
        attend[a] = b
    else:
        del attend[a]

# 남아있는 사람 이름 기준 사전 역순으로 정렬, 순서대로 출력 //or 사전 순 정렬, 역순으로 출력
attend = sorted(attend, reverse=True)
for i in attend:
    print(i)