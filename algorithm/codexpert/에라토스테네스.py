def era(n):
    arr = [0,0] + [1 for _ in range(n-1)]
    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = 0
    return [i for i in range(len(arr)) if arr[i]==1]

print(era(1989382793874839))