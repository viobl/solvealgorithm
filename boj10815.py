import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

dict = {}
for i in range(n):
    dict[card[i]] = 0

for j in range(m):
    if check[j] not in dict:
        print(0, end = ' ')
    else:
        print(1, end = ' ')


# # 이진탐색 - 왜 dict보다 더 오래걸릴까
# card.sort()
# def BinarySearch(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if array[mid] < target:
#             start = mid + 1
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             return mid
#     return False
#
# for i in range(m):
#     if BinarySearch(card, check[i], 0, n - 1) is not False:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')