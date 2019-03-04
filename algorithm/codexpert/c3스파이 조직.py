import sys
sys.stdin = open("c3스파이조직.txt")

n, code = input().split()
n = int(n)

stack = []
spy = []
cnt = 0
tt = 0
tmp = ''
for i in range(len(code)):
    if code[i]=='>':
        stack.pop()
        cnt -= 1
    elif code[i] == '<':
        stack.append(code[i])
        cnt += 1
    else:
        if code[i+1]!='>' and code[i+1]!='<':
            tmp += code[i]
            tt = 1
        else:
            if tt==0:
                spy.append([code[i], cnt])
            elif tt==1:
                tmp += code[i]
                spy.append([tmp, cnt])
                tt = 0
                tmp = ''

result = ''
for i in range(len(spy)):
    if spy[i][1] == n:
        result += spy[i][0] + ' '
print(result)