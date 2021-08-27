import sys

N = int(sys.stdin.readline())

arr = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, N+1):
    x, y, w, h = map(int, sys.stdin.readline().split())

    for k in range(x, x+w):
        for l in range(y, y+h):
            arr[k][l] = i

for j in range(1, N+1):
    total = 0

    for row in arr:
        total += row.count(j)

    print(total)