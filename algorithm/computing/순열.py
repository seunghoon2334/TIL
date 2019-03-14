def myprint(q):
    while q != 0:
        q -= 1
        print(" {}".format(T[q]), end='')
    print()
def permutation(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1,-1,-1):
            A[i], A[n-1] = A[n-1], A[i]
            T[r-1] = A[n-1]
            permutation(n-1, r-1, q)
            A[i], A[n-1] = A[n-1], A[i]

A = [1, 2, 3, 4]
T = [0] * 3
permutation(4, 3, 3)