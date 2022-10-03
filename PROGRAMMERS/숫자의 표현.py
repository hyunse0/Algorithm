# 프로그래머스 숫자의 표현

from math import sqrt

def solution(n):
    answer = 0
    
    for num in range(1, int(sqrt(n))+1):
        quotient, remainder = divmod(n, num)
        
        if not remainder:
            if quotient%2:
                answer += 1
            
            if quotient != n//quotient and (n//quotient)%2:
                answer += 1
    return answer

print(solution(10))