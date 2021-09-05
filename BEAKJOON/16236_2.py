# 백준 16263 아기 상어
from collections import deque

def find_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                # 상어의 위치도 다시 지나갈 수 있도록 0으로 바꿔주기
                arr[i][j] = 0
                return i, j


def eat_fish(x, y):
    global eat, time

    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1

    distance = 0
    before_distance = deque()
    before_distance.append((x, y))

    dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    for _ in range(N*N):
        # 상어로부터 같은 거리에 있는 물고기 좌표
        same_distance = deque()
        distance += 1

        while before_distance:
            curr_x, curr_y = before_distance.popleft()

            for dx, dy in dxy:
                nx, ny = curr_x+dx, curr_y+dy
                if nx in range(N) and ny in range(N):
                    visited[nx][ny] = 1
                    same_distance.append((nx, ny))

        # 같은 거리에 있는 물고기 중 먹을 수 있는 사이즈라면
        fish = []
        for i, j in same_distance:
            if arr[i][j] < size:
                fish.append((i, j))
        
        # 만약 먹을 수 있는 물고기가 존재한다면
        if fish:
            fish.sort(key=lambda x: (x[0], x[1]))
            fish_x, fish_y = fish[0]

            arr[fish_x][fish_y] = 0  # 잡아먹었으니까 물고기가 없는 것! 0으로 바꾸기
            eat += 1                 # 잡아먹은 물고기 수 체크
            time += distance         # 지금까지 움직인 거리(=시간) 더해주기
            return fish_x, fish_y
        else:
            before_distance = same_distance
    
    return 99, 99


N = int(input())
arr = [[i for i in map(int, input().split())] for _ in range(N)]

x, y = find_shark()
size = 2
eat = 0
time = 0

while x < 99 and y < 99:
    x, y = eat_fish(x, y)

    if eat == size:
        size += 1
        eat = 0

print(time)