import sys
sys.stdin = open('4261.txt')

t = int(input())
for tc in range(1,t+1):
    keypad = {'a':'2', 'b':'2', 'c':'2', 'd':'3', 'e':'3', 'f':'3',
              'g':'4', 'h':'4', 'i':'4', 'j':'5', 'k':'5', 'l':'5',
              'm':'6', 'n':'6', 'o':'6', 'p':'7', 'q':'7', 'r':'7', 's':'7',
              't':'8', 'u':'8', 'v':'8', 'w':'9', 'x':'9', 'y':'9', 'z':'9'}
    dial, n = input().split()
    n = int(n)
    array = input().split()
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(len(array[i])):
            if keypad[array[i][j]] == dial[j]:
               tmp += 1
            else:
                break
        if tmp == len(array[i]):
            cnt += 1

    print('#{} {}'.format(tc,cnt))
