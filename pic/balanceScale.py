# 양팔 저울
# 한 쪽에 그릇이 있고 물을 더 채워넣거나 추를 더 달 수 있다.
# 다른 한 쪽에는 추를 달 수 있음 왼/오/x 로 트리 3개로 구분
# 양 쪽 합쳐서 추의 개수는 입력되는 것에따라 정해져 있음
# 1~해당 추의 무게 다 합친 것 사이의 측정이 되지않는 자연수의 개수
def DFS(L, sum):
    if L == n:
        if 0 < sum <= s: # 음수를 고려하지 않아도 되는 이유=> 대칭으로 적용되는 가지 수 나옴
            res.add(sum)

    else:
        DFS(L + 1, sum + chu[L])
        DFS(L + 1, sum - chu[L])
        DFS(L + 1, sum)

n = int(input())
chu = list(map(int, input().split()))
s = sum(chu)
res = set() # 중복 제거 하면서 추가하는 자료구조
DFS(0, 0)
print(s - len(res))