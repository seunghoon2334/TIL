import sys
sys.stdin = open("e1쇠막대기.txt")

stack = []
s = input()
stick = 0
result = 0
for i in range(len(s)-1):
    if s[i]=='(':
        if s[i+1]==')':
            result += stick
        else:
            stick += 1
    elif s[i]==')':
        if s[i-1]=='(':
            pass
        else:
            result += 1
            stick -= 1
result += stick
print(result)
