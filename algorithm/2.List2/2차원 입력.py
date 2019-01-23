'''
3 4
0 1 0 0
0 0 0 0
0 0 1 0
'''

n, m = map(int, input().split())
mylist = [[0 for _ in range(m)] for _ in range(n)]
print()
print(mylist)
for i in range(n):
    mylist[i] = list(map(int, input().split()))
print(mylist)