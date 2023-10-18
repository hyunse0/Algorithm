# 백준 1208 부분수열의 합2

from itertools import combinations
from collections import defaultdict

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

mid = N//2
left = numbers[:mid]
right = numbers[mid:]

left_sum = defaultdict(int)
right_sum = defaultdict(int)

for i in range(len(left) + 1):
    for combo1 in combinations(left, i):
        left_sum[sum(combo1)] += 1

for j in range(len(right) + 1):
    for combo2 in combinations(right, j):
        right_sum[sum(combo2)] += 1

left_sum_num = sorted(left_sum.keys())
right_sum_num = sorted(right_sum.keys())

l_pointer = 0
r_pointer = len(right_sum_num) - 1
cnt = 0

while l_pointer < len(left_sum_num) and 0 <= r_pointer:
    temp = left_sum_num[l_pointer] + right_sum_num[r_pointer]

    if temp == S:
        cnt += left_sum[left_sum_num[l_pointer]] * right_sum[right_sum_num[r_pointer]]
        l_pointer += 1
        r_pointer -= 1
    elif temp > S:
        r_pointer -= 1
    else:
        l_pointer += 1

# 공집합 + 공집합인 경우 빼주기
if S == 0:
    cnt -= 1

print(cnt)