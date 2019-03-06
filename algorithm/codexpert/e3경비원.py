import sys
sys.stdin = open("e3경비원.txt")

width, height = map(int, input().split())
n = int(input())
arr = [[0 for _ in range(width+1)] for _ in range(height+1)]
for i in range(n):
    direction, d = map(int, input().split())
    if direction==1:
        arr[0][d]=1
    elif direction==2:
        arr[height][d]=1
    elif direction==3:
        arr[d][0]=1
    elif direction==4:
        arr[d][width]=1

start, startd = map(int, input().split())
if start==1:
    arr[0][startd]=2
    i = 0
    j = startd
elif start==2:
    arr[height][startd]=2
    i = height
    j = startd
elif start==3:
    arr[startd][0]=2
    i = startd
    j = 0
elif start==4:
    arr[startd][width]=2
    i = startd
    j = width

result1 = []
cnt = 0
if start==1:
    while j!=width:
        j += 1
        cnt += 1
        if arr[i][j]==1:
            result1.append(cnt)
    while i!=height:
        i += 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while j!=0:
        j -= 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while i!=0:
        i -= 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while j!=startd:
        j += 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
elif start==2:
    while j!=width:
        j += 1
        cnt += 1
        if arr[i][j]==1:
            result1.append(cnt)
    while i!=0:
        i -= 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while j!=0:
        j -= 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while i!=height:
        i += 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while j!=startd:
        j += 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
elif start==3:
    while i!=height:
        i += 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while j!=width:
        j += 1
        cnt += 1
        if arr[i][j]==1:
            result1.append(cnt)
    while i!=0:
        i -= 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while j!=0:
        j -= 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while i!=startd:
        i += 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
elif start==4:
    while i!=height:
        i += 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while j!=0:
        j -= 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while i!=0:
        i -= 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)
    while j!=width:
        j += 1
        cnt += 1
        if arr[i][j]==1:
            result1.append(cnt)
    while i!=startd:
        i += 1
        cnt += 1
        if arr[i][j] == 1:
            result1.append(cnt)

result = 0
for i in range(n):
    result += min(result1[i],cnt-result1[i])
print(result)



# width, height = map(int, input().split())
# n = int(input())
# stores = []
# for i in range(n):
#     direction, d = map(int, input().split())
#     stores.append([direction, d])
# start, startd = map(int, input().split())
#
# result = 0
# if start==1: #북
#     for i in range(len(stores)):
#         if stores[i][0]==1:
#             result += abs(startd-stores[i][1])
#         elif stores[i][0]==2:
#             result += height+min(startd+stores[i][1],(width-startd)+(width-stores[i][1]))
#         elif stores[i][0]==3:
#             result += startd+stores[i][1]
#         elif stores[i][0]==4:
#             result += (width-startd)+stores[i][1]
# elif start==2: #남
#     for i in range(len(stores)):
#         if stores[i][0]==1:
#             result += height+min(startd+stores[i][1],(width-startd)+(width-stores[i][1]))
#         elif stores[i][0]==2:
#             result += abs(startd-stores[i][1])
#         elif stores[i][0]==3:
#             result += (height-stores[i][1])+startd
#         elif stores[i][0]==4:
#             result += (width-startd)+(height-stores[i][1])
# elif start==3: #서
#     for i in range(len(stores)):
#         if stores[i][0]==1:
#             result += startd+stores[i][1]
#         elif stores[i][0]==2:
#             result += (height-startd)+stores[i][1]
#         elif stores[i][0]==3:
#             result += abs(startd-stores[i][1])
#         elif stores[i][0]==4:
#             result += width+min(startd+stores[i][1],(height-startd)+(height-stores[i][1]))
# elif start==4: #동
#     for i in range(len(stores)):
#         if stores[i][0]==1:
#             result += (width-startd)+stores[i][1]
#         elif stores[i][0]==2:
#             result += (height-startd)+(width-stores[i][1])
#         elif stores[i][0]==3:
#             result += width+min(startd+stores[i][1],(height-startd)+(height-stores[i][1]))
#         elif stores[i][0]==4:
#             result += abs(startd-stores[i][1])
# print(result)