def isWall(i,j):
    global tmp
    if tmp==0:
        if i-1==0 or arr[i-1][j]!=0:
            tmp = 1
            return True
    elif tmp==1:
        if j+1==jj+1 or arr[i][j+1]!=0:
            tmp = 2
            return True
    elif tmp==2:
        if i+1==ii+1 or arr[i+1][j]!=0:
            tmp = 3
            return True
    elif tmp==3:
        if j-1==0 or arr[i][j-1]!=0:
            tmp = 0
            return True
    return False

def go(i,j, tmp):
    if tmp==0:
        i -= 1
    elif tmp==1:
        j += 1
    elif tmp==2:
        i += 1
    elif tmp==3:
        j -= 1
    return [i,j]

jj, ii = map(int, input().split())
num = int(input())
tmp = 0
if num<=0 or num>(ii*jj):
    print(0)
else:
    arr = [[0 for _ in range(jj+2)] for _ in range(ii+2)]

    i = ii
    j = 1
    for cnt in range(1, (ii*jj)+1):
        arr[i][j] = cnt
        isWall(i,j)
        ij = go(i,j, tmp)
        i = ij[0]
        j = ij[1]

        if cnt==num:
            if tmp==0:
                print(j,ii-i)
                break
            elif tmp==1:
                print(j-1,ii-i+1)
                break
            elif tmp==2:
                print(j,ii-i+2)
                break
            elif tmp==3:
                print(j+1,ii-i+1)
                break


    # for p in range(ii+2):
    #     print(arr[p])