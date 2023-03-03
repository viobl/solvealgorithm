# m, n 받아와서 순열 만드는데 시간 복잡도가 그렇게 크지 않아보인다
# itertools 써서 하나씩 다 나열 쭉 해도 되겠다 근데 백트레킹을 활용하는 연습을 해야...
# 다 풀고, 4 4 case 되는데 안 되길래 어디가 틀렸지를 생각하며 구글링을 통해 재귀함수 리밋 재설정, readLine 수정 등을 하며 별의 별짓을 했는데...
# n, m 순서를 바꿔서 했었다....그러니 3번 케이스만 됐지
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline()

n, m = map(int, input.split())
s = []

# 중복 없이 1 ~ n개중 m개 고르기
def backTracking():
    # 출력 시점
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i in s: # 진행 여부 확인
            continue

        s.append(i)
        backTracking()
        s.pop() # pop 하고 다음 순서 진행

backTracking()