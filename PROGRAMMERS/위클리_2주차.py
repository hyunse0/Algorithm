# 프로그래머스 위클리 챌린지 2주차

def solution(scores):
    N = len(scores)

    r_scores = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            r_scores[x][y] = scores[y][x]

    answer = ''

    for i in range(N):
        max_score = max(r_scores[i])
        min_score = min(r_scores[i])

        student = N
        total = sum(r_scores[i])

        if r_scores[i][i] == max_score:
            if r_scores[i].count(max_score) == 1:
                student -= 1
                total -= max_score
        elif r_scores[i][i] == min_score:
            if r_scores[i].count(min_score) == 1:
                student -= 1
                total -= min_score
        
        mean = total/student

        print(mean)

        if mean >= 90:
            answer += 'A'
        elif mean >= 80:
            answer += 'B'
        elif mean >= 70:
            answer += 'C'
        elif mean >= 50:
            answer += 'D'
        else:
            answer += 'F'
            
    return answer

scores = [[50,90],[50,87]]
print(solution(scores))