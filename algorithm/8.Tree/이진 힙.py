import sys
sys.stdin = open("이진 힙.txt")

def enQ(n):
    global last
    last += 1
    c = last
    p = c//2
    Q[last] = n
    while c>1 and Q[p] > Q[c]:
        Q[p], Q[c] = Q[c], Q[p]
        c = p # 부모를 새로운 자식 노드로
        p = c//2
def deQ(n):
    global last
    r = Q[1] # 리턴값(루트노드)
    Q[1] = Q[last] # 마지막을 루트노드로 이동
    last -= 1 # 카운터 감소
    p = 1
    while p < last:
        c1 = p * 2 # 왼쪽자식
        c2 = p * 2 + 1 # 오른쪽 자식
        if c2 <= last: # 양쪽 자식이 다 있는 경우
            if Q[c1] < Q[c2]:
                c = c1
            else:
                c = c2
            if Q[c] < Q[p] : # 둘 중 작은쪽과 부모를 비교
                Q[c], Q[p] = Q[p], Q[c]
                p = c
            else:
                break
        elif c1 <= last: # 왼쪽 자식만 있는 경우
            if Q[c1] < Q[p]: # 둘 중 작은쪽과 부모를 비교
                Q[c1], Q[p] = Q[p], Q[c1]
                p = c1
            else:
                break
        else:
            break
    return r

def find():
    global N
    c = N
    p = c//2
    s = 0
    while p > 0:

