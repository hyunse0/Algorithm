# 백준 4485 녹색 옷 입은 애가 젤다지?

import sys

def dfs(x, y, amount):
    global answer, visited

    if amount >= answer:
        return
    
    if x == N-1 and y == N-1:
        answer = amount

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, amount+cave[nx][ny])
            visited[nx][ny] = 0


input = sys.stdin.readline

i = 1
while True:
    N = int(input())

    if not N:
        break

    cave = []
    for _ in range(N):
        cave.append(list(map(int, input().split())))
    
    answer = float('inf')
    
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 1

    dfs(0, 0, cave[0][0])

    print(f'Problem {i}: {answer}')
    i += 1