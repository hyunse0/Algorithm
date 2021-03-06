# 프로그래머스 보석 쇼핑

from collections import defaultdict

def solution(gems):
    if len(set(gems)) == 1:
        return [1, 1]
    
    locations = defaultdict(list)
    for i in range(len(gems)):
        locations[gems[i]].append(i)
    
    start = []
    end = []
    for location in locations.values():
        start.append(max(location))
        end.append(min(location))
        
    return [min(start)+1, max(end)+1]