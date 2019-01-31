import sys
sys.stdin = open("string.txt")

def mycount(word, a):
    cnt = 0
    for i in range(len(a)):
        if word==a[i]:
            cnt += 1
    return cnt

t = int(input())
for tc in range(t):
    str1 = list(set(input()))
    str2 = input()
    result = 0
    for i in range(len(str1)):
        if result < mycount(str1[i],str2):
            result = mycount(str1[i],str2)
    print(f'#{tc+1} {result}')

