def myprint(q):
    arr = [0, 0, 0]
    while q != 0:
        q -= 1
        arr[T[q]-1] = T[q]
    result.append(arr)

def combination(n, r, q):
    if r == 0:
        myprint(q)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        combination(n-1, r-1, q)
        combination(n-1, r, q)

A = [1, 2, 3]
T = [0] * 3

result = []
combination(3, 0, 0)
combination(3, 1, 3)
combination(3, 2, 3)
combination(3, 3, 3)
result.sort(reverse=True)
for i in range(len(result)):
    print(' '.join(map(str,result[i])))