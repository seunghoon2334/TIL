def fib(n):
    arr = [1, 1]
    if n==len(arr)+1:
        arr.append(arr[-1]+arr[-2])
    elif n>len(arr):
        while n!=len(arr):
            arr.append(arr[-1]+arr[-2])
    return arr[-1]

n = int(input())
print(fib(n))