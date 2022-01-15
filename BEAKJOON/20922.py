# 백준 20922 겹치는 건 싫어
from collections import defaultdict

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

idx = defaultdict(list)

max_len = 0
start = 0
end = 0

while True:
    # end 인덱스 1씩 증가
    while len(idx[numbers[end]]) < K:
        idx[numbers[end]].append(end)
        end += 1
        if end == N:
            break
    
    # 최장 길이 갱신
    max_len = max(max_len, end-start)
    if end == N:
        break

    # start 변경
    temp = idx[numbers[end]][0] + 1

    for i in range(start, temp):
        idx[numbers[i]].pop(0)
    
    start = temp

max_len = max(max_len, N-start)

print(max_len)