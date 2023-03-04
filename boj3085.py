# 색이 다른 인접한 두칸 고르기
# 연속 된 색이 같은 열 or 행 최대한 많이 먹기
# 처음에 한줄 다 같은 거 있으면 땡큐
# 각 행(다른 거 위아래 교환), 열(다른 거 양옆 교환) 연속되는 수 카운팅
# 범위 50으로 경우의 수 완전탐색 해볼만하다
def check(data):
    n = len(data)
    answer = 1

    for i in range(n):
        # 열 순회 연속 카운팅
        cnt = 1
        for j in range(1, n):
            if data[i][j] == data[i][j - 1]: # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 변동 후 다르면 다시 1로 초기화
                cnt = 1

            # answer 갱신
            if cnt > answer:
                answer = cnt

        # 행 순회 연속 카운팅
        cnt = 1
        for j in range(1, n):
            if data[j][i] == data[j - 1][i]:
                # 변동 전과 같으면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르면 다시 1로 초기화
                cnt = 1

            # cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt


    return answer

n = int(input())
data = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        # 행 바꾸기
        if i + 1 < n:
            data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]
            tmp = check(data)
            if tmp > answer:
                answer = tmp
            # 바꿨던걸 원래대로 되돌려야 하는데 이게 맞나
            # data[i + 1][j], data[i][j] = data[i][j], data[i + 1][j]
            data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]
        # 열 바꾸기
        if j + 1 < n:
            data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j]
            tmp = check(data)
            if tmp > answer:
                answer = tmp
            # 바꿨던걸 원래대로 되돌려야 하는데 이게 맞나
            data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j]


print(answer)