# 브루트포스
n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)

answer = 0

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())


def res(day, s):
    global answer

    # 종료 시기
    if day == n + 1:
        answer = max(s, answer)
        return

    # 퇴사일 오버 불가능
    if day > n + 1:
        return

    # 상담o
    res(day + t[day], s + p[day])

    # 상담x
    res(day + 1, s)


res(1, 0)
print(answer)