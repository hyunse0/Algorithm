# 백준 17070 파이프 옮기기 1

def push_pipe(i, j, state):
    global cnt 

    if i == N and j == N:
        cnt += 1
        return
    
    # 대각선으로 이동
    if i+1 <= N and j+1 <=N:
        if not house[i][j+1] and not house[i+1][j] and not house[i+1][j+1]:
            push_pipe(i+1, j+1, 'diagonal')
    
    # 가로로 이동
    if state != 'vertical':
        if j+1 <= N and not house[i][j+1]:
            push_pipe(i, j+1, 'horizon')
    
    # 세로로 이동
    if state != 'horizon':
        if i+1 <= N and not house[i+1][j]:
            push_pipe(i+1, j, 'vertical')


N = int(input())
house = [[0 for _ in range(N+1)]]
for _ in range(N):
    house.append([0] + list(map(int, input().split())))

cnt = 0
push_pipe(1, 2, 'horizon')

print(cnt)