# r 역순으로, d 첫항 버리기
# 입출력이 까다롭다
from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())

for testCase in range(tc):
    error = False
    reverse = False

    f = input().strip()
    cnt = int(input())
    nums = deque(input().strip()[1:-1].split(","))

    if cnt == 0:
        nums = deque()

    for cmd in f:
        if cmd == "R":
            if reverse:
                reverse = False
            else:
                reverse = True

        # R아니면 D만 있음
        else:
            if nums:
                if reverse:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                error = True
                break

    if error:
        print("error")

    elif reverse:
        nums.reverse()
        print("[" + ",".join(nums) + "]") # nums <= deque

    else:
        print("[" + ",".join(nums) + "]")