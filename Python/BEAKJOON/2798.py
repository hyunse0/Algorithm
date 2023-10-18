import sys

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

cards.sort(reverse=True)

card_sum = []
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_sum.append(cards[i] + cards[j] + cards[k])

max_sum = 0
for c_s in card_sum:
    if c_s <= M:
        if c_s > max_sum:
            max_sum = c_s

print(max_sum)