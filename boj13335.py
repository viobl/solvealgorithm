n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
t = 0

while bridge:
    t += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= l: # 대기중 트럭 제일 앞
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)

print(t)
