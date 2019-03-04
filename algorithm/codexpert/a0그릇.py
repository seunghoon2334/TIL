s = input()
result = 0
tmp = '-'
for i in s:
    if i != tmp:
        result += 10
        tmp = i
    else:
        result += 5
        tmp = i
print(result)