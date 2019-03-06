import sys
sys.stdin = open("d8초콜릿 공장.txt")

n = int(input())
result = 0
for nc in range(n):
    lchoco, hchoco = input().split()
    lcho = []
    hcho = []
    cnt = 0
    for i in lchoco:
        lcho.append(i)
    for i in hchoco:
        hcho.append(i)
    check = 0
    for i in lcho:
        if i in hcho:
            check += 1
    if check>=2:
        cnt += 1
    if cnt==0:
        setlcho = set(lcho)
        if not len(lcho)==len(setlcho):
            cnt += 1
        if cnt==0:
            sethcho = set(hcho)
            if not len(hcho) == len(sethcho):
                cnt += 1
    result += cnt
print(result)