string =  '2+3*4/5'
result = ''
stack = []
for i in string:
    if i=='+' or i=='-' or i=='*' or i=='/':
        stack.append(i)
    else:
        result += i + ' '
while stack != []:
    result += stack[-1] + ' '
    stack.pop()
print(result)