N, K = map(int, input().split())

students = {'1' : {'0' : 0, '1' : 0}, 
            '2' : {'0' : 0, '1' : 0},
            '3' : {'0' : 0, '1' : 0},
            '4' : {'0' : 0, '1' : 0},
            '5' : {'0' : 0, '1' : 0},
            '6' : {'0' : 0, '1' : 0}}

for _ in range(N):
    S, Y = input().split()

    students[Y][S] += 1

room = 0
for grade in range(1, 7):
    for sex in range(2):
        temp = students[str(grade)][str(sex)]
        if temp%K == 0:
            room += temp//K
        else:
            room += temp//K + 1

print(room)