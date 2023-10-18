# 백준 2638 치즈

from collections import deque

N, M = map(int, input().split())

cheese = []
for _ in range(N):
    cheese.append(list(map(int, input().split())))

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

answer = 0
while sum(map(sum, cheese)):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1

    queue = deque([(0, 0)])

    # 바깥 공기
    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M and not cheese[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    # 개수 세기
    cheese_cnt = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if cheese[i][j]:
                cnt = 0

                for di, dj in dxy:
                    ni, nj = i+di, j+dj

                    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                        cnt += 1
                
                cheese_cnt[i][j] = cnt
    
    # 녹는 치즈
    for i in range(N):
        for j in range(M):
            if cheese_cnt[i][j] < 3:
                cheese[i][j] = 0

    answer += 1

print(answer)