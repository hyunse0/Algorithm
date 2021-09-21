# 백준 7569 토마토

from collections import deque

def bfs(k, i, j):
    queue = deque()
    queue.append((k, i, j))

    visited = [[[0 * M] for _ in range(N)] for _ in range(H)]
    visited[k][i][j] = 1

    dxyz = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    while queue:
        z, x, y = queue.popleft()

        for dz, dx, dy in dxyz:
            nz, nx, ny = z+dz, x+dx, y+dy

            if 0 <= nz < H and 0 <= nx < M and 0 <= ny < N and not visited[nz][nx][ny]:
                visited[nz][nx][ny] = 1
                queue.append((nz, nx, ny))

                if box[nz][nx][ny] == 1:
                    if box[z][x][y] == 0:
                        box[z][x][y] = 1

    return


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(box)
cnt = 0
bfs(0, 0, 0)
print(box)
