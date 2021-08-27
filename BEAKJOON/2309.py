from itertools import combinations

high = []

for _ in range(9):
    high.append(int(input()))

high.sort()


for subset in combinations(high, 7):
    if sum(subset) == 100:
        break

for i in range(7):
    print(subset[i])