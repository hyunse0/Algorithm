T = int(input())

for t in range(1, T+1) :
    N = int(input())

    snail = []
    for _ in range(N) :
        snail.append(list(0 for __ in range(N)))

    i = 0
    j = 0
    line = 0
    way = 0

    for n in range(1, N*N + 1) :
        if way%4 == 0 :
            if j < N  :
                snail[i][j] = n
                j += 1
            else :
                i += 1
                j -= 1
                way += 1
                snail[i][j] = n
                i += 1
        elif way%4 == 1 :
            if i < N :
                snail[i][j] = n
                i += 1
            else :
                i -= 1
                j -= 1
                way += 1
                snail[i][j] = n
                j -= 1
        elif way%4 == 2 :
            if j >= line :
                snail[i][j] = n
                j -= 1
            else :
                i -= 1
                j += 1
                way += 1
                snail[i][j] = n
                i -= 1
        elif way%4 == 3 :
            if i > line :
                snail[i][j] = n
                i -= 1
            else :
                i += 1
                j += 1
                way += 1
                snail[i][j] = n
                j += 1
        
                line += 1
                N -= 1

    print(f'#{t}')
    
    for I in range(len(snail[0])) :
        for J in range(len(snail[0])) :
            if J == len(snail[0]) - 1 :
                print(snail[I][J])
            else :
                print(snail[I][J], end=' ')