T = int(input())

for t in range(1, T+1) :
    N = int(input())
    
    v = 0
    distance = 0
    for n in range(N) :
        command_list = list(map(int, input().split()))

        if command_list[0] == 1 :
            v += command_list[1]
        elif command_list[0] == 2 :
            if v < command_list[1] :
                v = 0
            else :
                v -= command_list[1]

        distance += v

    print(f'#{t} {distance}')