# 백준 1520 내리막 길
import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global result

    if x == M-1 and y == N-1:
        result += 1
        return

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy

        if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] < arr[x][y]:
            dfs(nx, ny)
    

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = 0
dfs(0, 0)
print(result)