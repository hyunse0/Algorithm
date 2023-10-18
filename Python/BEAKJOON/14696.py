N = int(input())

def game(a, b):
    a4 , b4 = a.count(4), b.count(4)
    a3 , b3 = a.count(3), b.count(3)
    a2 , b2 = a.count(2), b.count(2)
    a1 , b1 = a.count(1), b.count(1)

    if a4 != b4:
        if a4 > b4:
            return 'A'
        else:
            return 'B'
    elif a3 != b3:
        if a3 > b3:
            return 'A'
        else:
            return 'B'
    elif a2 != b2:
        if a2 > b2:
            return 'A'
        else:
            return 'B'
    elif a1 != b1:
        if a1 > b1:
            return 'A'
        else:
            return 'B'
    else:
        return 'D'


for _ in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_shape = a[1:]
    b_shape = b[1:]

    a_shape.sort()
    b_shape.sort()

    print(game(a_shape, b_shape))

