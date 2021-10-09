# 프로그래머스 위클리 챌린지 3주차
from collections import defaultdict, deque

def turn_left(arr):
    N = len(arr)
    
    temp = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            print(i, j, N-1-i)
            temp[i][j] = arr[j][N-1-i]
    
    return temp


def bfs(i, j, arr, flag):
    N = len(arr)
    
    queue = deque()
    queue.append((i, j))
    
    path = [(i, j)]
    
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[i][j] = 1
    
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == flag:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                
                path.append((nx, ny))
    
    # 퍼즐조각을 포함한 직사각형 배열
    i_lst = []
    j_lst = []
    for i, j in path:
        i_lst.append(i)
        j_lst.append(j)
    
    temp = [[0 for _ in range(max(j_lst)-min(j_lst)+1)] for _ in range(max(i_lst)-min(i_lst)+1)]
    for i, j in path:
        temp[i-min(i_lst)][j-min(j_lst)] = 1
        arr[i][j] = 0
        
    return temp, len(path)


def solution(game_board, table):
    N = len(game_board)
    
    puzzle = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if table[i][j]:
                temp, cnt = bfs(i, j, table, 1)
                puzzle[cnt].append(temp)
    
    answer = 0
    
    for k in range(N):
        for l in range(N):
            if not game_board[k][l]:
                space, s_cnt = bfs(k, l, game_board, 0)
                
                for idx in range(len(puzzle[cnt])):
                    for _ in range(4):
                        if space == puzzle[cnt][idx]:
                            answer += 1
                            puzzle[cnt].pop(idx)
                        else:
                            turn_left(space)
                            
    return answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

print(solution(game_board, table))