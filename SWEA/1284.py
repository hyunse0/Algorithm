T = int(input())
i = 0

for _ in range(T) :
    i += 1
    p, q, r, s, w = map(int, input().split())

    A = p * w
    
    if w <= r :
        B = q
    else :
        B = q + (w - r) * s

    if A >= B :
        print(f'#{i} {B}')
    else :
        print(f'#{i} {A}')