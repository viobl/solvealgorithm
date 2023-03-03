# n x n 정사각 체스판에 queen n 개 놓는 경우의 수
# n = int(input()) 시간 초과
import sys
n = int(sys.stdin.readline())
answer = 0
row = [0] * n

def condition(x):
    for i in range(x):
        # 같은 행/열, 대각 불가능
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True

def nQueen(x):
    global answer # 전역변수 설정해야 함수에서 읽을 수 있음
    if x == n:
        answer += 1
    else:
        for i in range(n):
            row[x] = i # 퀸 놓는 자리설정
            if condition(x): # parameter 잊지말자
                nQueen(x + 1)

nQueen(0)
print(answer)