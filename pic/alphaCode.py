# 숫자 입력 받아서 스플릿하고 해당 번호를 알파벳으로 변경하여 출력
# 한자리면 해당 알파벳으로 치환
# 두자리받아서 26이하면 다른 알파벳으로도 치환 가능
def DFS(L, p):
    global cnt
    if L == n:
        cnt += 1
        for j in range(p):
            print(chr(res[j] + 64), end = '')
        print()

    else:
        for i in range(1, 27):
            if code[L] == i: # 한자리 숫자
                res[p] = i
                DFS(L + 1, p + 1)

            elif i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                res[p] = i
                DFS(L + 2, p + 1)


code = list(map(int, input()))
n = len(code)
code.insert(n, -1) # 두자리로 입력할때 리스트 오버되므로 -1
res = [0] * (n + 3)
cnt = 0
DFS(0, 0)
print(cnt)