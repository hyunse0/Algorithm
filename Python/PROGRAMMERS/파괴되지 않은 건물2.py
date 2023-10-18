# 프로그래머스 파괴되지 않은 건물
# 누적합

def solution(board, skill):
    summary = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree
        
        summary[r1][c1] += degree
        summary[r1][c2+1] -= degree
        summary[r2+1][c1] -= degree
        summary[r2+1][c2+1] += degree

    for i in range(len(board)):
        for j in range(len(board[0])):
            summary[i+1][j] += summary[i][j]
            
    for j in range(len(board)):
        for i in range(len(board[0])):
            summary[i][j+1] += summary[i][j]
                    
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j] + summary[i][j] > 0:
                answer += 1
                
    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))