# 무게 c 넘지 않으면서 바둑이 w 최대한 많이 태우기
import sys
# sys.stdin=open("input.txt", "r")
def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])


if __name__=="__main__":
    c, n=map(int, input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0, 0, 0)
    print(result)


# 전체 c, 마리 수 n
# 무게 입력 받아오기
# dfs 이용해서 넘은것 작은 것 부터 하나씩 뺐다 넣었다
