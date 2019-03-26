def myprint(q):
    t = []
    while q != 0:
        q -= 1
        t.append(T[q])
    result.append(t)

def permutation(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1,-1,-1):
            A[i], A[n-1] = A[n-1], A[i]
            T[r-1] = A[n-1]
            permutation(n-1, r-1, q)
            A[i], A[n-1] = A[n-1], A[i]

A = [1, 2, 3]
T = [0] * 3
result = []
permutation(3, 3, 3)
result.sort()
for i in range(len(result)):
    print(' '.join(map(str,result[i])))