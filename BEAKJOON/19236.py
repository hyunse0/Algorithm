# 백준 19236 청소년 상어

def move_fish(num, way):
    new_space = [[0 for _ in range(4)] for _ in range(4)]
    new_numbers = {}

    x, y = numbers[num]

    while True:
        nx, ny = x+dxy[way][0], y+dxy[way][1]
        if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
            new_space[nx][ny] = (num, way)
            new_space[x][y] = space[nx][ny]
            new_numbers[space[x][y][0]] = (x, y)
            new_numbers[space[nx][ny][0]] = (nx, ny)
            return new_space, new_numbers
        else:
            if way == 7: way -= 8
            way += 1


def move_shark(eat, space, numbers):
    global shark, way, visited, answer

    # 상어가 물고기를 잡아먹음
    eat += space[shark[0]][shark[1]][0]
    way = space[shark[0]][shark[1]][1]
    numbers.pop(space[shark[0]][shark[1]][0])
    space[shark[0]][shark[1]] = 0
    visited[shark[0]][shark[1]] = 1

    # 물고기 이동
    for num, fish in numbers.items():
        new_space, new_numbers = move_fish(num, space[fish[0]][fish[1]][1])
    
    # 상어 이동
    while True:
        x, y = shark[0], shark[1]
        nx, ny = x+dxy[way][0], y+dxy[way][1]

        if 0 <= nx < 4 and 0 <= ny < 4 and space[nx][ny][0]:
            shark = (nx, ny)
            move_shark(eat, new_space, new_numbers)
            shark = (x, y)
            
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

shark = (0, 0)
way = (-1, -1)

answer = 0
move_shark(0, space, numbers)
print(answer)