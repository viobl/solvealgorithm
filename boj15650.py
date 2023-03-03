# 15649와 유사하지만 중복은 제거
# 역시나 itertools 활용하면 더 쉽지만 따로 백트레킹을 활용하는 방식으로
# n, m 파라미터 순서 잊지말고 백트레킹 잘 하자
n, m = map(int, input().split())
s = []
def backTracking(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            backTracking(i + 1)
            s.pop()

backTracking(1)