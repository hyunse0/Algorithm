T = int(input())

for t in range(T) :
    a, b = map(int, input().split())
    print(f'#{t+1} {a//b} {a%b}')