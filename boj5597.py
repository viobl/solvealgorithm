# 사람 수 만큼 리스트 만들때 사용하는 방식
student = [i for i in range(1, 31)]

for _ in range(28):
    check = int(input())
    student.remove(check)

print(min(student))
print(max(student))