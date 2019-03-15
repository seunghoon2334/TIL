
M = int(input())
mo =[]
for i in range(M):
    mo.append(list(map(int, input())))

P = int(input())
pa =[]
for i in range(P):
    pa.append(list(map(int, input())))

def check(i, j):
    for k in range(P):  # 패턴의 행
        for l in range(P):  # 패턴의 열
            if mo[i + k][j + l] != pa[k][l]: return 0
    # 모두 패턴이 일치하면 같은 패턴 찾았으므로 sol 카운트
    return 1

cnt=0
sol=0
for i in range(M-P+1): #모눈중이의 시작행 제어
    for j in range(M-P+1): #모눈종이의 시작열 제어
        if check( i, j )==1: sol+=1
print(sol)