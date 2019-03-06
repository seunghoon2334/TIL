time = []
money = 0
for i in range(5):
    stime, etime = map(float, input().split())
    estime = etime - stime - 1
    if estime <= 0:
        time.append(0.0)
    elif estime >= 4:
        time.append(4.0)
    else:
        time.append(estime)

for i in range(5):
    money += time[i] * 10000
if sum(time) >= 15:
    money *= 0.95
elif sum(time) <= 5:
    money *= 1.05
print(int(money))