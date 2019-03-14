import sys
sys.stdin = open("190214workshop.txt")

for tc in range(1,11):
    V, E = map(int, input().split())
    nums = list(map(int, input().split()))

    G = [[0 for i in range(V + 1)] for j in range(V + 1)]
    for i in range(0, len(nums), 2):
        G[nums[i]][nums[i+1]] =1
    # s = []
    key = [0 for i in range(V + 1)]
    key2 = [[0 for i in range(V + 1)] for j in range(V + 1)]
    a = []
    while len(a)!=V:
        for i in range(1,V+1):
            if G[i]==key and i not in a:
                # s.append(i)
                a.append(i)
                for j in range(1,V+1):
                    G[j][i]=0

    result = f'#{} '
    for i in range(len(a),0,-1):
        result += str(a[i-1]) + ' '
    print(result)





