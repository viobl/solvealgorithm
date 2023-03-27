# 크로아티아 알파벳 : 지정된 크로아티아 알파벳을 변환, 변환한 알파벳 카운트
s = input()
croatianAlpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 하나하나 if 문으로 바꿔서 카운팅 vs 길이만 필요하니 대체하고 길이만 프린팅하기
for i in croatianAlpha:
    s = s.replace(i, '*')  # input 바꾸고 길이 체크
print(len(s))