def prime(n):
    nums = [0,0] + [1 for _ in range(n-1)]
    for i in range(2,n+1):
        if nums[i]==1:
            for j in range(i*2,n+1,i):
                nums[j] = 0
    for i in range(2, n + 1):
        if nums[i] == 1:
            print('{}'.format(i), end=" ")

prime(1000000)