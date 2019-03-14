def combination(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return combination(n-1, r-1) + combination(n-1, r)

def fac(n):
    arr = [1, 1]
    cnt = len(arr)
    while len(arr)-1!=n:
        arr.append(arr[-1]*cnt)
        cnt += 1
    return arr[n]

def combi(n, r):
    return fac(n)//(fac(n-r)*fac(r))

# print(combi(100, 50))
print(combination(100, 50))