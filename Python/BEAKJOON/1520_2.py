# 백준 1520 내리막 길
def dfs(x, y, temp):
    global result

    visited = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            visited[i][j] = temp[i][j]

    if x == M-1 and y == N-1:
        result += 1
        return 

    visited[x][y] = 1

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy

        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] < arr[x][y]:
            dfs(nx, ny, visited)
    

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
temp = [[0 for _ in range(N)] for _ in range(M)]

result = 0
dfs(0, 0, temp)

print(result)