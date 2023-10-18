# 프로그래머스 파괴되지 않은 건물
# 완전 탐색 : 효율성 0점

def solution(board, skill):
    for t, r1, c1, r2, c2, degree in skill:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if t == 1:
                    board[i][j] -= degree
                else:
                    board[i][j] += degree
                    
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j] > 0:
                answer += 1
                
    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))