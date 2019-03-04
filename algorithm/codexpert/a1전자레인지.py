t = int(input())
a = 0
b = 0
c = 0
result = 0
while t!=0 and result==0:
    if t>=300:
        t -= 300
        a += 1
    elif t>=60:
        t -= 60
        b += 1
    elif t>=10:
        t -= 10
        c += 1
    else:
        result = -1
if result==-1:
    print(result)
else:
    print(a, b, c)