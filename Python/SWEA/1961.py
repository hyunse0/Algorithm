T = int(input())

for t in range(1, T+1) :
    N = int(input())

    arrange = [[], [], [], []]


    for _ in range(N) :
        arrange[0].append(list(map(int, input().split())))

    for cnt in range(3) :

        for j in range(N) :
            temp = []
            for i in range(N-1, -1, -1) :
                temp.append(arrange[cnt][i][j])

            arrange[cnt+1].append(temp)
        
    print(f'#{t}')
    for arr_i in range(N) :
        for n in range(1, 4) :
            for arr_j in range(N) :
                print(arrange[n][arr_i][arr_j], end = '')
            print(' ', end = '')
        print('')