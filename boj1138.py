n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        # 제일 큰 사람은 왼쪽에 있는 사람수 +1
        if cnt == arr[i] and answer[j] == 0:
            answer[j] = i + 1
            break

        # 자신 키 순위랑 왼쪽에 있는 0개수 같은 경우
        elif answer[j] == 0:
            cnt += 1

print(' '.join(map(str, answer)))