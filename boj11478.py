s = input()
a = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        a.add(s[i : j + 1]) # 슬라이스로 순차 추가

print(len(a))