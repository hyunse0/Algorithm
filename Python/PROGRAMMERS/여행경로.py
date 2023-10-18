from collections import defaultdict

def solution(tickets):
    airport = defaultdict(list)
    
    for ticket in tickets:
        airport[ticket[0]].append(ticket[1])
        
    answer = []
    def dfs(v, way):
        nonlocal answer
        
        if answer:
            return
        
        if len(way) == len(tickets)+1:
            answer = way
            return
        
        for w in sorted(airport[v]):
            airport[v].remove(w)
            dfs(w, way+[w])
            airport[v].append(w)
    
    dfs('ICN', ['ICN'])
    
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))