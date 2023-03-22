# stack
# input 받아올때 다 string, 끝날때 . 공백없이 들어옴
# 균형은 소괄호, 대괄호가 둘다 온전하게 있어야 성립
# stack에 넣어두고 온점 나오면 반환하는 형식으로 진행
import sys
input = sys.stdin.readline

while True:
    s = input().rstrip() # readline 쓸때 rstrip 안하니 오류가 자주 나온다
    stack = []

    # 온점 나오면 종료
    if s == '.':
        break

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':  # stack 안 지우고 가져오기만 할때는 stack[-1]
                stack.pop()
            else:
                stack.append(')')
                break

        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break

    # stack 에 따라 프린팅
    if len(stack) == 0:
        print('yes')
    else:
        print('no')