import sys
sys.stdin = open('input.txt')

def bfs(i, j):
    queue = [(i, j)]
    arr[i][j] = 0

    dxy = [(1, 0), (0, 1)] # 아래, 오른쪽

    while queue:
        x, y = queue.pop(0)

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if nx in range(N) and ny in range(N) and arr[nx][ny]:
                arr[nx][ny] = 0
                queue.append((nx, ny))

    return x, y


T = int(input())

for t in range(1, 11):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    subset = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                x, y = bfs(i, j)
                subset.append((x-i+1, y-j+1))

    subset.sort(key=lambda x : (x[0]*x[1], x[0]))

    print('#{} {}'.format(t, len(subset)), end=' ')
    for i in range(len(subset)):
        if i == len(subset) - 1:
            print(*subset[i])
        else:
            print(*subset[i], end=' ')