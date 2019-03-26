def nsum(n):
    if n<len(arr):
        return arr[n]
    elif n==len(arr):
        arr.append(arr[-1]+n)
        return arr[-1]
    else:
        return nsum(n-1) + n

arr = [0, 1]
n = int(input())
print(nsum(n))