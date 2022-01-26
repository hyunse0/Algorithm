# 프로그래머스 입국심사

import heapq

def solution(n, times):
    heap = []
    for t in times:
        heapq.heappush(heap, (t, t))
    
    person = 1
    while person < n:
        endtime, time = heapq.heappop(heap)
        heapq.heappush(heap, (endtime+time, time))
        person += 1
    
    return heapq.heappop(heap)[0]