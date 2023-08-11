import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start = 1
end = max(lan)

while(start <= end):
    mid = (start + end) // 2 #절단 기준 설정
    cnt = 0

    for i in range(k):
        cnt += lan[i] // mid

    # n보다 커서 최대 길이가 성립하지 않을 가능성이 높은 경우
    if cnt >= n:
        start = mid + 1 # 기준 이하 값 필요x
    else:
        end = mid - 1 # 기준 이상 값 필요x

print(end)