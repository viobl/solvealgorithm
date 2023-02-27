n = int(input())

for i in range(n):
    ox = list(input())
    score = 0
    totalScore = 0
    for j in ox:
        if j == 'O':
            score += 1 # 연속 정답 시 추가 점수

        else:
            score = 0 # 정답 끊길 때 점수 초기화
        totalScore += score
    print(totalScore)
