# 백준 18405 경쟁적 전염

from collections import deque, defaultdict

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

numbers = defaultdict(deque)
for i in range(N):
    for j in range(N):
        if board[i][j]:
            numbers[board[i][j]].append((i, j))

virus = sorted(numbers.keys())

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(S):
    for num in virus:
        cnt = len(numbers[num])
        for _ in range(cnt):
            x, y = numbers[num].popleft()

            for dx, dy in dxy:
                nx, ny = x+dx, y+dy

                if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
                    board[nx][ny] = num
                    numbers[num].append((nx, ny))

print(board[X-1][Y-1])