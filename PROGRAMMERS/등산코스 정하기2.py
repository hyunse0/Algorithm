# 프로그래머스 등산코스 정하기
# 출입구에서 산봉우리까지 *2
# 다익스트라

from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):

    def dijkstra():
        heap = []

        for gate in gates:
            heapq.heappush(heap, (0, gate)) # intensity, gate
            intensity[gate] = 0

        while heap:
            i, v = heapq.heappop(heap)

            if v in summits or i > intensity[v]:
                continue

            for w, d in graph[v]:
                new_i = max(i, d)

                if new_i < intensity[w]:
                    heapq.heappush(heap, (new_i, w))
                    intensity[w] = new_i

    
    # set은 in 연산을 할 경우 시간 복잡도가 O(1)
    summits = set(summits)

    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    intensity = [float('inf') for _ in range(n+1)]
    dijkstra()

    answer = [float('inf'), float('inf')]
    for summit in sorted(summits):
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
    
    return answer


paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
print(solution(6, paths, [1, 3], [5]))