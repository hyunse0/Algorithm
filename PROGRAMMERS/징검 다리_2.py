# 프로그래머스 징검다리

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    s, e = 0, distance
    
    while s <= e:
        mid = (s+e)//2
        cnt = 0
        this = 0
        
        for rock in rocks:
            if rock - this < mid:
                cnt += 1
            else:
                this = rock
            
        if cnt > n:
            e = mid - 1
        else:
            answer = mid
            s = mid + 1
        
    return answer