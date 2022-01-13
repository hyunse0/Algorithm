# 프로그래머스 합승 택시 요금

from collections import deque

def solution(n, s, a, b, fares):
    def find_min_dist(end):
        queue = deque()
        queue.append(s)
        
        visited = [0 for _ in range(n+1)]
        visited[s] = 1
        
        way = []
        
        while queue:
            v = queue.popleft()
            if v == end:
                return way
            
            for w, c in cost[v]:
                if not visited[w]:
                    visited[w] = 1
                    queue.append(w)
                    way.append((w, c))
                    break
            
    
    cost = [[] for _ in range(n+1)]
    for fare in fares:
        i, j, c = fare
        cost[i].append((j, c))
        cost[j].append((i, c))
    
    for i in range(1, n+1):
        cost[i] = sorted(cost[i], key=lambda x: x[1])
    
    way_a = deque(find_min_dist(a))
    way_b = deque(find_min_dist(b))
    way_ab = []
    
    while way_a and way_b and way_a[0] == way_b[0]:
        way_ab.append(way_a.popleft())
        way_b.popleft()
    
    answer = 0
    for way in (way_a, way_b, way_ab):
        for p, c in way:
            answer += c
            
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))