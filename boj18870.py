# 좌표압축 이라길래 상대좌표화 시켜서 계산하는 건 줄 알았는데 아니다.
# 들어온 상수 받아서 순서대로 나열 하고
# 동일 수라면 앞에 오는 인덱스의 값으로 받아온다.
# 하나씩 쭉 나열 하고 카운팅해서 수 올리고 해당 인덱스 값 출력? => dict
import sys # 단위 백만

n = int(input())
xCaps = list(map(int, sys.stdin.readline().rstrip().split()))

xSet = set(xCaps)
a = list(xSet)
a.sort()

xDict = {}
for i in range(len(a)): # 딕셔너리 배열에 삽입, 인덱스화
    xDict[a[i]] = i

for i in xCaps: # 좌표 압축한거 인덱스대로 출력
    print(xDict[i], end=' ')