n, m = map(int, input().split())
log = list(map(int, input().split()))
start = 1
end = max(log)
while(start <= end):
    mid = (start + end) // 2

    total = 0
    for i in log:
        if i >= mid:
            total += i - mid

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)