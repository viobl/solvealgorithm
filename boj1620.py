import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocket = {}

for i in range(1, n + 1):
    a = input().rstrip() # 공백제거 필요
    pocket[i] = a
    pocket[a] = i

for _ in range(m):
    question = input().rstrip()
    if question.isdigit(): # 10진법 수인지 확인
        print(pocket[int(question)])
    else:
        print(pocket[question])