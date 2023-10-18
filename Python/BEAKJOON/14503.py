# 백준 14503 로봇 청소기

def what_is_d(dx, dy):
    if dx == 0 and dy == -1:
        return 3
    elif dx == 1 and dy == 0:
        return 0
    elif dx == 0 and dy == 1:
        return 1
    else:
        return 2


def dfs(x, y, d):
    global cnt, dxy

    in_dxy = dxy[d:d+4]
    flag = True

    for dx, dy in in_dxy:
        nx, ny = x+dx, y+dy

        if place[nx][ny] == 0:
            place[nx][ny] = 2
            cnt += 1
            dfs(nx, ny, what_is_d(dx, dy))
            flag = False
            break

    if flag:
        # 후진
        dx, dy = in_dxy[1]
        bx, by = x-dx, y-dy

        if place[bx][by] != 1:
            dfs(bx, by, d)


N, M = map(int, input().split())
# d / 0 : 북(-서) , 1 : 동쪽(-북), 2 : 남쪽(-동), 3 : 서쪽(-남)
r, c, d = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(N)]

# 서 남 동 북 서 남
dxy = [(0, -1), (-1, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (0, -1)]

place[r][c] = 2
cnt = 1
dfs(r, c, d)
print(cnt)