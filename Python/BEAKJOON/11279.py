# 백준 11279 최대 힙

import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque()

for _ in range(N):
    num = int(sys.stdin.readline())

    if num:
        arr.append(num)
    else:
        if arr:
            max_num = max(arr)
            arr.remove(max_num)
            print(max_num)
        else:
            print(0)