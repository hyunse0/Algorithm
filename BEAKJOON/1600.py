# 백준 1600 말이 되고픈 원숭이

from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j, 0, [(i, j)]))

    temp_dxy = [(1, 0), (-1, 0), (0, 1), (0, -1),
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (-1, 2), (1, -2), (-1, -2)]

    while queue:
        curr_x, curr_y, cnt, visited = queue.popleft()

        if curr_x == W-1 and curr_y == H-1:
            return len(visited) - 1

        if cnt == K:
            dxy = temp_dxy[:4]
        else:
            dxy = temp_dxy
        
        for dx, dy in dxy:
            each_cnt = cnt

            if dx == 2 or dy == 2:
                each_cnt += 1

            nx, ny = curr_x + dx, curr_y + dy

            if nx in range(W) and ny in range(H) and (nx, ny) not in visited and board[nx][ny] == 0:
                queue.append((nx, ny, each_cnt, visited + [(nx, ny)]))

    return -1


K = int(input())
W, H = map(int, input().split())

board = []
for _ in range(W):
    board.append(list(map(int, input().split())))

print(bfs(0, 0))