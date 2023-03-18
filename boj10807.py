# 개수세기 배열식? 리스트에 하나씩 하는 건지 => count로 한번에
n = int(input())
nums = list(map(int, input().split()))
v = int(input())

print(nums.count(v))
