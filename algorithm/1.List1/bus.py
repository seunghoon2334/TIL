import sys
sys.stdin = open("bus.txt")

t = int(input())
for i in range(t):
    tc = list(map(int, input().split()))
    k = tc[0] #한번 충전으로 이동 가능한 정류장 수
    n = tc[1] #종점 번호
    m = tc[2] #충전기 설치된 정류장 갯수
    charge = list(map(int, input().split()))
    # 충전기 설치된 정류장 번호
    result = 1
    point = k#버스현위치
    cnt = 0
    fail = 0
    while point < n: #0부터 출발해서 k만큼 가고 충전가능하면 충전 후 출발 아니면 뒤로 한칸씩 이동하다가 제자리면 0출력
        #충전소인가 비교
        if point in charge:
            cnt += 1
            point += k
        else :
            point -= 1
            fail += 1
            if fail == n:
                result = 0
                break
    if result==0:
        print(f'#{i+1} 0')
    else:
        print(f'#{i+1} {cnt}')