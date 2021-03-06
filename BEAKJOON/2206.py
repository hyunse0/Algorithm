# 백준 2206 벽 부수고 이동하기

import sys
sys.setrecursionlimit(99999)

def dfs(x, y, wall, dist):
    global answer

    if x == N-1 and y == M-1:
        answer = min(answer, dist)
        return

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if not grid[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, wall, dist+1)
                visited[nx][ny] = 0
            
            if not wall and grid[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, 1, dist+1)
                visited[nx][ny] = 0


N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, list(input()))))

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

answer = float('inf')

dfs(0, 0, 0, 1)

if answer == float('inf'):
    print(-1)
else:
    print(answer)