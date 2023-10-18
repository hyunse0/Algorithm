# 백준 2096 내려가기

N = int(input())

max_sum = min_sum = list(map(int, input().split()))

for _ in range(N-1):
    input_num = list(map(int, input().split()))

    max_sum = [input_num[0] + max(max_sum[:2]), input_num[1] + max(max_sum), input_num[2] + max(max_sum[1:])]
    min_sum = [input_num[0] + min(min_sum[:2]), input_num[1] + min(min_sum), input_num[2] + min(min_sum[1:])]

print(max(max_sum), min(min_sum))