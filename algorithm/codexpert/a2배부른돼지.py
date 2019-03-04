n = int(input())
yes = []
no = []
if n == 0:
    print('F')
else:
    for nc in range(n):
        num, yn = input().split()
        if yn=='N':
            no.append(int(num))
        else :
            yes.append(int(num))
    maxno = max(no)
    minyes = min(yes)
    if maxno>minyes:
        print('F')
    else:
        print(maxno+1)