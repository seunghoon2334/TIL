import sys
sys.stdin = open('베이비진 게임.txt')

def babygin(player):
    for i in range(len(player)-2):
        if player[i]==player[i+1]==player[i+2]:
            return 1
    player = list(set(player))
    player.sort()
    if len(player)>=3:
        for i in range(len(player)-2):
            if player[i]+2 == player[i + 1]+1 == player[i + 2]:
                return 1
    return 0

t = int(input())
for tc in range(1,t+1):
    arr = list(map(int,input().split()))
    player1 = [arr[0], arr[2]]
    player2 = [arr[1], arr[3]]
    one = 0
    two = 0
    for i in range(4,12,1):
        if i%2==0:
            player1.append(arr[i])
            player1.sort()
            one = babygin(player1)
        else:
            player2.append(arr[i])
            player2.sort()
            two = babygin(player2)
        if one==1 or two==1:
            break
    if one==two==0:
        print('#{} {}'.format(tc,0))
    elif one==1:
        print('#{} {}'.format(tc,1))
    else:
        print('#{} {}'.format(tc,2))