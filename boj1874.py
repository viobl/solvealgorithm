# n개의 줄에 +, - 하나씩해서 스택 만드는 과정 출력
import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans =[]
cnt = 1
flag = 0

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    # stack에 넣고 빼낼때
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in ans:
        print(i) # idx에서 바로 출력


