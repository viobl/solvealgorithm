# 4바이트 당 long + int 붙이기

n = int(input())

for i in range(n // 4):
    print("long", end=" ")
print("int")
