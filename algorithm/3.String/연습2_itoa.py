def itoa(x):
    str = list()

    while x != 0:
        r = x % 10
        str.append(chr(r + ord('0')))
        x //= 10

    str.reverse()
    str = "".join(str)
    return str

x = 123;
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))

