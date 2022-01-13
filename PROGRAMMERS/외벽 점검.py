# 프로그래머스 외벽 점검

from itertools import permutations
from collections import deque

def solution(n, weak, dist):
    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i]+n)
        
    for i in range(weak_len):
        now = i
        end = i + weak_len - 1
        
        answer = 0
        for friend in permutations(dist, len(dist)):
            friend = deque(friend)
            cnt = 0
            flag = False
            while friend:
                able_dist = friend[now] + friend.popleft()
                cnt += 1
                while friend[now] <= able_dist:
                    now += 1
                    if now == end:
                        answer = min(answer, cnt)
                        flag = True
                        break
                if flag:
                    break
            
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))