# 프로그래머스 등산코스 정하기
# 출입구에서 산봉우리까지 *2
# 완전 탐색 : 런타임 에러, 시간초과

from collections import defaultdict

def solution(n, paths, gates, summits):

    def hiking(v, intensity):
        nonlocal answer

        # 가지치기
        if intensity > answer[1]:
            return
        
        # answer 갱신
        if v in summits:
            if intensity == answer[1] and v > answer[0]:
                return
            
            answer = [v, intensity]
            return
        
        for w, d in graph[v]:
            if not visited[w] and w not in gates and d <= answer[1]:
                visited[w] = 1
                hiking(w, max(intensity, d))
                visited[w] = 0

    
    # set은 in 연산을 할 경우 시간 복잡도가 O(1)
    gates = set(gates)
    summits = set(summits)
    
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    answer = [float('inf'), float('inf')]

    for gate in gates:
        visited = [0 for _ in range(n+1)]
        hiking(gate, 0)
    
    return answer

paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
print(solution(6, paths, [1, 3], [5]))