s, x = input().split()
x = int(x)

result = 'NONE'
for i in range(1, len(s)):
    a = int(s[:i])
    b = int(s[i:])
    if a < x and b < x:
        if a + b == x:
            result = str(a) + '+' + str(b) + '=' + str(x)
print(result)