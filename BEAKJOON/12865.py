# 백준 12865 평범한 배낭

from itertools import combinations

N, K = map(int, input().split())

things = {} # key : 무게 / value : 가치
for _ in range(N):
    W, V = map(int, input().split())
    things[W] = V

subset = []
for r in range(N+1):
    for combo in combinations(things.keys(), r):
        if sum(combo) <= K:
            subset.append(combo)

max_v = 0
for combo in subset:
    temp = 0
    for n in combo:
        temp += things[n]
    
    if temp > max_v:
        max_v = temp

print(max_v)