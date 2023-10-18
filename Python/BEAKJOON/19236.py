# 백준 19236 청소년 상어

import copy

def move_fish(num, way, space, numbers, shark):
    x, y = numbers[num]

    while True:
        nx, ny = x+dxy[way][0], y+dxy[way][1]
        if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != shark:
            space[x][y], space[nx][ny] = space[nx][ny], space[x][y]
            numbers[space[x][y][0]] = (x, y)
            numbers[space[nx][ny][0]] = (nx, ny)
            return space, numbers
        else:
            if way == 7: way -= 8
            way += 1


def move_shark(x, y, way, eat, before, numbers):
    global visited, answer

    after = copy.deepcopy(before)
    after_numbers = numbers.copy()
    
    # 상어가 물고기를 잡아먹음
    eat += after[x][y][0]
    way = after[x][y][1]
    after_numbers.pop(after[x][y][0])
    after[x][y] = 0
    visited[x][y] = 1

    # 물고기 이동
    for num, fish in after_numbers.items():
        after, after_numbers = move_fish(num, after[fish[0]][fish[1]][1], after, after_numbers, (x, y))
    
    # 상어 이동
    while True:
        nx, ny = x+dxy[way][0], y+dxy[way][1]

        if 0 <= nx < 4 and 0 <= ny < 4 and space[nx][ny][0]:
            move_shark(nx, ny, way, eat, after, after_numbers)
        else:
            answer = max(answer, eat)
            return


space = []
numbers = {} # 숫자의 현재 위치
for i in range(4):
    temp = list(map(int, input().split()))
    row = []

    for j in range(0, 8, 2):
        row.append((temp[j], temp[j+1]-1))
        numbers[temp[j]] = (i, j//2)
    
    space.append(row)

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dxy = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
visited = [[0 for _ in range(4)] for _ in range(4)]

answer = 0
move_shark(0, 0, -1, 0, space, numbers)
print(answer)