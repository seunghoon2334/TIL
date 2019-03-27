arr=[1,2,4,7,8,3]
# arr=[6,6,7,7,6,7]
# arr=[0,5,4,0,6,0]
# arr=[1,0,1,1,2,3]

def BabyGin(arr):
    global flag
    tmp = 0
    if arr[0]==arr[1]==arr[2]:
        tmp += 1
    elif arr[0]+1==arr[1]==arr[2]-1:
        tmp += 1
    if arr[3]==arr[4]==arr[5]:
        tmp += 1
    elif arr[3]+1==arr[4]==arr[5]-1:
        tmp += 1
    if tmp==2:
        flag = 1
        print(arr)
        return 1
    else:
        return

def perm(n,k):
    if n==k:
        if BabyGin(arr):
            return
    else:
        for i in range(k,n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n,k+1)
            arr[i], arr[k] = arr[k], arr[i]

flag = 0
perm(6,0)

if flag:
    print('BabyGin')
else:
    print('Not BabyGin')