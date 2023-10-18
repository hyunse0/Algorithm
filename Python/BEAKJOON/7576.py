# 백준 7576 토마토

from collections import deque

def bfs(i, j):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
    
    max_day = 0
    for i in range(N):
        for j in range(M):
            if not box[i][j]:
                return -1
            
            if box[i][j] > max_day:
                max_day = box[i][j]
    
    return max_day - 1


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

print(bfs(0, 0))