# 백준 20922 겹치는 건 싫어
from collections import defaultdict

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = defaultdict(int)
idx = defaultdict(list)

max_len = 0
start = 0
for i in range(N):
    cnt[numbers[i]] += 1    
    idx[numbers[i]].append(i)

    if cnt[numbers[i]] > K:
        max_len = max(max_len, i-start)

        temp = idx[numbers[i]].pop(0) + 1
        for j in range(start, temp):
            cnt[numbers[j]] -= 1

        start = temp

max_len = max(max_len, N-start)

print(max_len)