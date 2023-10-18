import sys
from typing import NoReturn

N = int(sys.stdin.readline())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 선택 정렬
for i in range(len(numbers)-1):
    min_idx = i
    for j in range(i, len(numbers)):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

for number in numbers:
    print(number)