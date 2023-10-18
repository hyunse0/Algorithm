# 백준 5556 타일

N = int(input())
K = int(input())
tiles = [list(map(int, input().split())) for _ in range(K)]

for i, j in tiles:
    if i > (N+1)/2:
        i = N+1-i
    
    if j > (N+1)/2:
        j = N+1-j
    
    if i > j:
        answer = j%3
    else:
        answer = i%3
    
    if answer == 0:
        answer = 3
    
    print(answer)