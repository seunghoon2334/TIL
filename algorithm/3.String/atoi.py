def atoi(string):
    value = 0
    i = 0
    while (i < len(string)): # chr(int) , ord(str)
        c = string[i]
        if c >= '0' and c <= '9':
            digit = ord(c) - ord('0')
        else:
            break
        value = (value * 10) + digit;
        i += 1
    return value

a = "123"
print(type(a), a)
b = atoi(a)
print(type(b), b)
c = int(a)
print(type(c), c)


str1 = 'abc 1'
str1.replace('1', 'one')
print(str1)