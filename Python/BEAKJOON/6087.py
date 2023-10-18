# 백준 6087 레이저 통신

def dfs(x, y, way, cnt):
    global answer

    if cnt >= answer:
        return
    
    if (x, y) != start and grid[x][y] == 'C':
        answer = cnt
        return
    
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy

        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and (grid[nx][ny] == '.' or grid[nx][ny] == 'C'):
            visited[nx][ny] = 1

            if (dx, dy) == way:
                new_cnt = cnt
            else:
                new_cnt = cnt+1

            dfs(nx, ny, (dx, dy), new_cnt)

            visited[nx][ny] = 0


W, H = map(int, input().split())
grid = [list(input()) for _ in range(H)]

start = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'C':
            start = (i, j)
            break
    
    if start:
        break

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = [[0 for _ in range(W)] for _ in range(H)]
visited[start[0]][start[1]] = 1

answer = float('inf')

dfs(start[0], start[1], (-1, -1), -1)

print(answer)