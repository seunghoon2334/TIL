def my_strrev(ary):
    a = list(ary)
    for i in range(len(ary)//2+1):
        a[i], a[-1-i] = a[-1-i], a[i]

    return "".join(a)

ary = "abcde"
ary = my_strrev(ary)
print(ary)

s = "Reverse this strings"
s = s[::-1]
print(s)