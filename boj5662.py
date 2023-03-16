# boj5662;
alpaList = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

sec = 0
for unit in alpaList: # 리스트에서 하나씩 분리
    for i in unit:
        for x in word:
            if i == x:
                sec += alpaList.index(unit) + 3
print(sec)