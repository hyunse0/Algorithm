T = int(input())

for t in range(T) :
    numbers = list(map(int, input().split()))
    max_num = 0

    for num in numbers :
        if num > max_num :
            max_num = num
    
    print(f'#{t+1} {max_num}')