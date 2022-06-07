# 백준 2477 참외밭

K = int(input())

x = []
y = []

for i in range(6):
    way, length = map(int, input().split())

    if way == 1 or way == 2:
        y.append((i, length))
    else:
        x.append((i, length))

x.sort(key=lambda z: -z[1])
y.sort(key=lambda z: -z[1])

mx = x[0][1]
mxi = x[0][0]

my = y[0][1]
myi = y[0][0]

mxim = mxi - 1
mxip = mxi + 1

myim = myi - 1
myip = myi + 1

if mxi == 0:
    mxim = 5
elif mxi == 5:
    mxip = 0

if myi == 0:
    myim = 5
elif myi == 5:
    myip = 0

for i, s in x[1:]:
    if i != myim and i != myip:
        sx = s

for i, s in y[1:]:
    if i != mxim and i != mxip:
        sy = s

width = (mx * my) - (sx * sy)
print(K * width)