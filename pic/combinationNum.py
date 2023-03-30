# 수들의 조합
# n개의 정수 k개 뽑아서 더하기 m의 배수
# 인수의 개수가 증가하는 원인 생각해보기
def DFS(L, s, sum): # 시작하는 원소
    global cnt
    # l, k 같을 때 종료
    if L == k:
        # m의 배수 카운팅
        if sum % m == 0:
            cnt += 1
    else:
        # 중복 없이 늘려가면서 더하고 조회하기
        for i in range(s, n):
            DFS(L + 1, i + 1, sum + a[i])

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0
DFS(0, 0, 0)
print(cnt)