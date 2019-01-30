# def itoa(x):
#     a = ['0','1','2','3','4','5','6','7','8','9']
#     s = ''
#     while x != 0:
#         s += a[x % 10]
#         x //= 10
#
#     return s[::-1]

def itoa(x):
    str = list()

    while x != 0:
        r = x % 10
        str.append(chr(r + ord('0')))
        x //= 10

    str.reverse()
    str = ''.join(str)
    return str

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))