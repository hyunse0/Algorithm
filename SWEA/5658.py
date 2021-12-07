# SWEA 5658 보물상자 비밀번호
from collections import deque

def four_num(num):
    global total

    i = 0
    for _ in range(4):
        temp = ''
        for j in range(i, i+cnt):
            temp += num[j]
            
        total.append(temp)
        i += cnt


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    num = deque(input())

    cnt = N//4
    total = []

    for _ in range(cnt):
        four_num(num)
        num.append(num.popleft())
    
    total = list(set(total))
    total.sort(reverse=True)
    target = int(total[K-1], 16)

    print('#{} {}'.format(t, target))