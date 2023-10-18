import sys

def bfs(n):
    global cnt
    
    queue = [(0, 0)]
    dxy = [(0, 1), (1, 0)]

    visited = [[0 for _ in range(1001)] for _ in range(1001)]
    visited[0][0] = 1

    while queue:
        x, y = queue.pop(0)
        if arr[x][y] == n:
            cnt += 1

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if nx in range(1001) and ny in range(1001) and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))


N = int(sys.stdin.readline())

arr = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, N+1):
    x, y, w, h = map(int, sys.stdin.readline().split())

    for k in range(x, x+w):
        for l in range(y, y+h):
            arr[k][l] = i

for j in range(1, N+1):
    cnt = 0
    bfs(j)

    print(cnt)