n = int(input())#학생수
nums = list(map(int,input().split()))#번호뽑기
line = []#줄서있
cnt = 1
while cnt!=n+1:
    line.append(cnt)
    cnt += 1
for i in range(n):
    if nums[i]==0:
        pass
    else:
        line.pop(i)
        line.insert(i-nums[i],i+1)

result = ''
for i in line:
    result += str(i) + ' '
print(result)