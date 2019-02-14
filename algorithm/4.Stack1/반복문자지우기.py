import sys
sys.stdin = open("반복문자지우기.txt")

t = int(input())
for tc in range(t):
    s = input()
    s = list(s)
    result=1
    while result!=0:
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                s.pop(i+1)
                s.pop(i)
                result=1
                break
            result=0
        if len(s) <= 1:
            break
    print(f'#{tc+1} {len(s)}')