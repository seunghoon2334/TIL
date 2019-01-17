y=[1,2,3,4,5,6,7,8,9]
for i in range(int(input())):
        a=[list(map(int,input().split())) for i in range(9)]
        b=list(zip(*a))
        t=0
        for j in range(9):
                if sorted(a[j])==y and sorted(b[j])==y:
                        t+=1
        for m in range(0,9,3):
                for k in range(0,9,3):
                        c=a[m][k:k+3]+a[m+1][k:k+3]+a[m+2][k:k+3]
                        if sorted(c)==y:
                                t+=1
        [print(f'#{i+1} 1')if t==18 else print(f'#{i+1} 0')]