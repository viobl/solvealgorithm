# 바이토닉 수열 단조증가 후 단조감소
# 단조 증가 후 단조 감소 수열 최대길이
# 단조 증가 수열 중 최대 길이
# 단조 감소 수열 중 최대 길이 비교 => 이게 맞나? 시간복잡도 절차적 중복이 있는거 아닌가
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ra = a[::-1]
# 자기 자신 단일항일 경우에도 증감수열이라 볼 수 있으므로 카운팅하고 시작
inc = [1] * n
dec = [1] * n
res = [0] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]: # 증가 수열 변동사항 확인
            inc[i] = max(inc[i], inc[j] + 1)
        if ra[i] > ra[j]: # 감소 수열 변동사항 확인
            dec[i] = max(dec[i], dec[j] + 1)

for i in range(n):
    res[i] = inc[i] + dec[n - i - 1] - 1 # , 최대값 중복 계산하므로 -1

print(max(res))