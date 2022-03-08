# 백준 2146 다리 만들기

from collections import deque

def find_island(i, j):
    queue = deque()
    queue.append((i, j))

    island_visited[i][j] = 1

    temp = set()

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < N and not island_visited[nx][ny]:
                if grid[nx][ny]:
                    island_visited[nx][ny] = 1
                    queue.append((nx, ny))
                else:
                    temp.add((x, y, 0))
    
    return temp


def linked_island(land):
    global min_dist

    queue = deque(land)

    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i, j, d in land:
        visited[i][j] = 1

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                if grid[nx][ny] and dist >= 1:
                    min_dist = min(min_dist, dist)
                    return
                elif not grid[nx][ny]:
                    queue.append((nx, ny, dist+1))


N = int(input())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 섬찾기
island = []
island_visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not island_visited[i][j] and grid[i][j]:
            island.append(find_island(i, j))

# 섬 별 거리 찾기
min_dist = float('inf')
for land in island:
    linked_island(land)

print(min_dist)