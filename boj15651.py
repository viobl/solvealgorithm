# 15649, 15650 과 문제 비슷하지만 중복 선택이 가능, 수열 자체가 중복은 불가능
# 중복 가능하게 하려면 무엇을 어떻게 바꾸어서 풀어야할까

n, m = map(int, input().split())
s = []

def bfs():
    # 출력 시점
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # 리스트에 추가 중복 가능
    # list idx 0 ~ m-1 까지 각각 설정하는 걸로 생각했다가 기존에 했던 것에서 중복 체크만 없어도 가능하지 않나 싶게 됨
    for i in range(1, n + 1):
        s.append(i)
        bfs()
        s.pop()

bfs()
