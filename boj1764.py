import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = {}
for i in range(n):
    tmp = input().rstrip() # readline을 적용했을 때 공백을 처리해야하는 예가 있는듯하다.
    a[i] = tmp

b = {}
for i in range(m):
    tmp = input().rstrip()
    b[i] = tmp

# dict는 교집합을 활용 못 함 => set으로 변환하여 적용
av = set(a.values())
bv = set(b.values())
answer = sorted(av & bv)

lenAns = len(answer)
print(lenAns)
for i in range(lenAns):
    print(answer[i])

# test
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton