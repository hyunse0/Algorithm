# 백준 2096 내려가기
import sys 
sys.setrecursionlimit(9999999)

def dfs(x, y, sum):
    global min_sum, max_sum
    
    if x == N-1:
        min_sum = min(min_sum, sum)
        max_sum = max(max_sum, sum)
        return

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < 3:
            dfs(nx, ny, sum+number[nx][ny])


N = int(input())
dxy = [(1, -1), (1, 0), (1, 1)]
number = [list(map(int, input().split())) for _ in range(N)]

min_sum = float('inf')
max_sum = 0

dfs(0, 0, number[0][0])
dfs(0, 1, number[0][1])
dfs(0, 2, number[0][2])

print(max_sum, min_sum)