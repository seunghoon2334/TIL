import sys
sys.stdin = open("sort.txt")

def selectionSort(a):
    cnt = 0
    for i in range(0, len(a)-1):
        if i%2==1:
            min = i
            for j in range(i+1, len(a)):
                if a[min] > a[j]:
                    min = j
            a[i], a[min] = a[min], a[i]
            cnt += 1
        else:
            max = i
            for j in range(i+1, len(a)):
                if a[max] < a[j]:
                    max = j
            a[i], a[max] = a[max], a[i]
            cnt += 1
        if cnt==10:
            break

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        selectionSort(arr)
    s = '#'
    s += str(tc+1) + ' '
    for ii in range(10):
        s += str(arr[ii]) + ' '
    print(s)
