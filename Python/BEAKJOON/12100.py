# 백준 12100 2048

def move(x, y, dx, dy, board):
    num = board[x][y]

    while True:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < N:
            if not board[nx][ny]:
                board[x][y], board[nx][ny] = 0, num
            elif board[nx][ny] == num:
                board[x][y], board[nx][ny] = 0, num*2
            else:
                return
            
            x, y = nx, ny


def top(board):
    for i in range(1, N):
        for j in range(N):
            move(i, j, -1, 0, board)
    
    return board


def bottom(board):
    for i in range(N-2, -1, -1):
        for j in range(N):
            move(i, j, 1, 0, board)

    return board

def left(board):
    for j in range(1, N):
        for i in range(N):
            move(i, j, 0, -1, board)
    
    return board


def right(board):
    for j in range(N-2, -1, -1):
        for i in range(N):
            move(i, j, 0, 1, board)

    return board


def find_max(board, cnt):
    global answer

    answer = max(answer, max(map(max, board)))

    if cnt == 5:
        return
    
    # find_max(top(board), cnt+1)
    # find_max(bottom(board), cnt+1)
    find_max(left(board), cnt+1)
    find_max(right(board), cnt+1)


N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = 0

if N == 1:
    answer = board[0][0]
else:
    find_max(board, 0)

print(answer)