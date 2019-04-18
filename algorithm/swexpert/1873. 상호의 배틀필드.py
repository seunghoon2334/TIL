import sys
sys.stdin = open('1873.txt')

def up(i,j):
    if i!=0 and field[i-1][j]=='.':
        field[i][j] = '.'
        field[i-1][j] = '^'
        return [i-1,j]
    else:
        field[i][j] = '^'
        return [i,j]

def down(i,j):
    if i!=h-1 and field[i+1][j]=='.':
        field[i][j] = '.'
        field[i+1][j] = 'v'
        return [i+1,j]
    else:
        field[i][j] = 'v'
        return [i, j]

def left(i,j):
    if j!=0 and field[i][j-1]=='.':
        field[i][j] = '.'
        field[i][j-1] = '<'
        return [i,j-1]
    else:
        field[i][j] = '<'
        return [i, j]

def right(i,j):
    if j!=w-1 and field[i][j+1]=='.':
        field[i][j] = '.'
        field[i][j+1] = '>'
        return [i,j+1]
    else:
        field[i][j] = '>'
        return [i, j]

def shoot(i,j):
    if field[i][j]=='^':
        if i==0:
            return
        else:
            while i!=0:
                i -= 1
                if field[i][j]=='.' or field[i][j]=='-':
                    pass
                elif field[i][j]=='*':
                    field[i][j] = '.'
                    return
                else:
                    return
    elif field[i][j]=='v':
        if i==h-1:
            return
        else:
            while i != h-1:
                i += 1
                if field[i][j] == '.' or field[i][j] == '-':
                    pass
                elif field[i][j] == '*':
                    field[i][j] = '.'
                    return
                else:
                    return
    elif field[i][j]=='<':
        if j==0:
            return
        else:
            while j != 0:
                j -= 1
                if field[i][j] == '.' or field[i][j] == '-':
                    pass
                elif field[i][j] == '*':
                    field[i][j] = '.'
                    return
                else:
                    return
    elif field[i][j]=='>':
        if j==w-1:
            return
        else:
            while j != w-1:
                j += 1
                if field[i][j] == '.' or field[i][j] == '-':
                    pass
                elif field[i][j] == '*':
                    field[i][j] = '.'
                    return
                else:
                    return

t = int(input())
for tc in range(1, t+1):
    h, w = map(int, input().split()) # 높이 너비
    field = []
    for i in range(h):
        s = input()
        field.append(list(''.join(map(str, s))))
    # print(field)
    a, b = -1, -1
    for i in range(h):
        for j in range(w):
            if field[i][j]=='^' or field[i][j]=='v' or field[i][j]=='<' or field[i][j]=='>':
                a, b = i, j
                break
        if a!=-1 and b!=-1:
            break

    n = int(input())
    ns = input()
    for n in ns:
        if n=='U':
            ab = up(a,b)
        elif n=='D':
            ab = down(a,b)
        elif n=='L':
            ab = left(a,b)
        elif n=='R':
            ab = right(a,b)
        else:
            shoot(a,b)
            ab = [a, b]
        a, b = ab[0], ab[1]
    string = ''
    for j in range(w):
        string += field[0][j]
    print('#{} {}'.format(tc,string))
    for i in range(1,h):
        string = ''
        for j in range(w):
            string += field[i][j]
        print(string)