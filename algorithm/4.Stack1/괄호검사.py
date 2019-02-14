import sys
sys.stdin = open("괄호검사.txt")

def push(item):
    s.append(item)

def pop():
    if len(s)==0:
        return -1
    else:
        return s.pop(-1)

def rhkfgh(string):
    for i in string:
        if i=='(' or i=='{' or i=='[':
            push(i)
        elif i==')':
            tmp = pop()
            if tmp==-1 or tmp!='(':
                return 0
        elif i=='}':
            tmp = pop()
            if tmp==-1 or tmp!='{':
                return 0
        elif i==']':
            tmp = pop()
            if tmp==-1 or tmp!='[':
                return 0
    if s==[]:
        return 1
    else:
        return 0

t = int(input())
for tc in range(t):
    string = input()
    s = []
    print(f'#{tc+1} {rhkfgh(string)}')