import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    ch = int(input())
    k = list(map(int, input().split()))
    # DP활용을 위한 2차원 행렬로 적용
    board = [[0] * ch for _ in range(ch)]

    for i in range(ch - 1):
        # idx에 따라 누적합 board23 = k2 + k3
        board[i][i + 1] = k[i] + k[i + 1]
        for j in range(i + 2, ch):
            board[i][j] = board[i][j - 1] + k[j]

    # 대각선 상으로 최소 누적합 기록
    for slash in range(2, ch):
        for q in range(ch - slash):
            r = slash + q
            res = [board[q][ch] + board[ch][r] for ch in range(q, r)]
            board[q][r] += min(res)

    print(board[0][ch - 1])