import sys

N = int(sys.stdin.readline())

cnt = [0]*10000

for _ in range(N):
    cnt[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if cnt[i]:
        for _ in range(cnt[i]):
            print(i+1)