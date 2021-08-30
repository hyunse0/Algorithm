from collections import defaultdict

N = int(input())
temp = list(map(int, input().split()))
switch = defaultdict(bool)

for i in range(1, N+1):
    switch[i] = bool(temp[i-1])


for _ in range(int(input())):
    sex, card = map(int, input().split())

    if sex == 1:
        for i in range(1, N+1):
            if i % card == 0:
                switch[i] = not switch[i]
    
    else:
        switch[card] = not switch[card]

        j = 1
        while card-j in range(1, N+1) and card+j in range(1, N+1):
            if switch[card-j] == switch[card+j]:
                switch[card-j] = not switch[card-j]
                switch[card+j] = not switch[card+j]
                j += 1

            else:
                break


for key, value in switch.items():
    if key == N or key%20 == 0:
        print(int(value))
    else:
        print(int(value), end=' ')