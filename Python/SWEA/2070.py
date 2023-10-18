T = int(input())

for t in range(T) :
    a, b = map(int, input().split())
    if a > b :
        print(f'#{t+1} >')
    elif a == b :
        print(f'#{t+1} =')
    else :
        print(f'#{t+1} <')