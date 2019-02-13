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
                return False
        elif i=='}':
            tmp = pop()
            if tmp==-1 or tmp!='{':
                return False
        elif i==']':
            tmp = pop()
            if tmp==-1 or tmp!='[':
                return False
    if s==[]:
        return True
    else:
        return False


s = []
string1 = '(a(b)'
string2 = 'a(b)c)'
string3 = 'a{b(c[d]e}f)'
string4 = 'a(b)c'
string5 = '()(){(){[]}}'

s = []
print(rhkfgh(string1))
s = []
print(rhkfgh(string2))
s = []
print(rhkfgh(string3))
s = []
print(rhkfgh(string4))
s = []
print(rhkfgh(string5))