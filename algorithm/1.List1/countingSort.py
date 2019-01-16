def countingSort(a, b, c):
    for i in range(len(a)):
        c[a[i]] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]

    for i in range(len(a)-1,-1,-1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1


a = [5, 8, 7, 1, 1, 5, 4, 1]
b = [0] *len(a)
c = [0] * 10
countingSort(a, b, c)
print(b)