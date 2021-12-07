# SWEA 2382 미생물 격리
from collections import defaultdict

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    group = {}
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

    for _ in range(K):
        i, j, n, d = map(int, input().split())
        group[(i, j)] = [n, dxy[d-1]]

    for _ in range(M):
        temp = defaultdict(list)
        for place, info in group.items():
            temp[(place[0]+info[1][0], place[1]+info[1][1])].append((place[0], place[1]))
        
        after_move = {}
        for after, before in temp.items():
            if len(before) >= 2:
                max_n = 0
                total = 0
                way = (-1, -1)
                for b in before:
                    if group[b][0] > max_n:
                        max_n = group[b][0]
                        way = group[b][1]
                    
                    total += group[b][0]
                
                after_move[after] = [total, way]
            elif 0 in after or N-1 in after:
                after_move[after] = [group[before[0]][0]//2, (-group[before[0]][1][0], -group[before[0]][1][1])]
            else:
                after_move[after] = group[before[0]]

        group = after_move

    answer = 0
    for n, d in group.values():
        answer += n
    
    print('#{} {}'.format(t, answer))