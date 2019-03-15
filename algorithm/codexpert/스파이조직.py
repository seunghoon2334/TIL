import sys
sys.stdin = open("in.txt")

N, arr=input().split()
N = int(N)
dep=0
i=0
while i<len(arr):
    if arr[i]=='<': dep+=1
    elif arr[i] =='>': dep-=1
    else:
        if dep==N:
            for j in range(i, i+5):
                if arr[j]=='<' or arr[j]=='>':
                    break
                else :
                    print(arr[j], end='')
            i = j - 1
            #print('i=%d' % i, end=' ')
            print(end=' ')
    i+=1


