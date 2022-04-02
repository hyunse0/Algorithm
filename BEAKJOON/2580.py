# 백준 2580 스도쿠

from copy import deepcopy

def horizon(numbers, i, sudoku):
    for num in sudoku[i]:
        if num in numbers:
            numbers.remove(num)
    
    return numbers


def vertical(numbers, j, sudoku):
    if len(numbers) == 1:
        return numbers

    for i in range(9):
        num = sudoku[i][j]

        if num in numbers:
            numbers.remove(num)
    
    return numbers


def square(numbers, i, j, sudoku):
    if len(numbers) == 1:
        return numbers

    ri = i%3
    rj = j%3

    if ri == 0:
        si = i
    elif ri == 1:
        si = i-1
    else:
        si = i -2

    if rj == 0:
        sj = j
    elif rj == 1:
        sj = j-1
    else:
        sj = j -2

    for x in range(si, si+3):
        for y in range(sj, sj+3):
            if sudoku[x][y] in numbers:
                numbers.remove(sudoku[x][y])
    
    return numbers


def filled_number(sudoku):
    global answer

    this = deepcopy(sudoku)

    flag = True
    for i in range(9):
        for j in range(9):
            if not this[i][j]:
                numbers = [x for x in range(1, 10)]
                numbers = horizon(numbers, i, this)
                numbers = vertical(numbers, j, this)
                numbers = square(numbers, i, j, this)

                if numbers:
                    flag = False
                    for num in numbers:
                        this[i][j] = num
                        filled_number(this)
                else:
                    return

    if flag:
        answer = this
        return


sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

answer = []
filled_number(sudoku)

for i in range(9):
    print(' '.join(map(str, answer[i])))