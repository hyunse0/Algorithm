# 프로그래머스 정수 삼각형

def solution(triangle):
    for i in range(len(triangle)-1):
        temp = [0 for _ in range(len(triangle[i+1]))]

        for j in range(len(triangle[i])):
            temp[j] = max(temp[j], triangle[i+1][j] + triangle[i][j])
            temp[j+1] = max(temp[j+1], triangle[i+1][j+1] + triangle[i][j])

        triangle[i+1] = temp
        
    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))