'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
'''
s = list()
def push(item):
    s.append(item)
def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)
def isEmpty():
    if len(s) == 0: return True
    else: return False

def check_matching(data):
    for i in range(len(data)): #문자열 스캔
        if data[i] == "(":     #왼쪽괄호
            push(data[i])
        elif data[i] == ")":   #오른쪽괄호
            if isEmpty(): return False
            pop()
    if not isEmpty(): return False
    else: return True

data = input()
print(check_matching(data))


