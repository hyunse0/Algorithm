# 프로그래머스 징검다리 건너기 -> 효율성 0점

def solution(stones, k):
    answer = 0
    while True:
        jump = 0
        for i in range(len(stones)):
            if stones[i] == 0:
                jump += 1
                if jump >= k:
                    break
            else:
                jump = 0
                stones[i] -= 1
        
        if jump >= k:
            return answer
        else:
            answer += 1

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
print(solution(stones, 3))