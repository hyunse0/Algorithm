# 프로그래머스 크레인 인형뽑기 게임
# 행, 열 변환 있는 버전 : 테스트 11 〉	통과 (0.21ms, 10.1MB) -> 이게 더 빠르다!

from collections import defaultdict, deque

def solution(board, moves):
    # 행, 열 바꾸기
    new_board = defaultdict(deque)
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]:
                new_board[j+1].append(board[i][j])
                
    answer = 0
    basket = []
    
    for move in moves:
        if new_board[move]:
            doll = new_board[move].popleft()
            
            if basket and basket[-1] == doll:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))