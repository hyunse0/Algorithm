# 백준 1987 알파벳

import sys
from collections import deque

def bfs():
    global answer

    queue = deque()
    queue.append((0, 0, [alphabet[0][0]]))

    while queue:
        x, y, path = queue.popleft()
        answer = max(answer, len(path))

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 <= nx < R and 0 <= ny < C and alphabet[nx][ny] not in path:
                queue.append((nx, ny, path+[alphabet[nx][ny]]))


input = sys.stdin.readline

R, C = map(int, input().split())
alphabet = [list(input()) for _ in range(R)]

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

answer = 0
bfs()

print(answer)