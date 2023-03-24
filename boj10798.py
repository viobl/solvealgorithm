# 세로 읽기
# 각 인덱스 0번부터 최대 15번까지 순서대로 쭉 프린팅

# 다 생성하고 시작
m = [[0] * 15 for i in range(5)]

for i in range(5):
    s = list(input())
    sList = len(s)

    for j in range(sList):
        m[i][j] = s[j]

for i in range(15):
    for j in range(5):
        # 값 없으면 패스
        if m[j][i] == 0:
            continue;
        else:
            print(m[j][i], end='')
