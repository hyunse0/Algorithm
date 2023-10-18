string = input()

number = []
for s in string:
    if s in 'ABC':
        number.append(2)
    elif s in 'DEF':
        number.append(3)
    elif s in 'GHI':
        number.append(4)
    elif s in 'JKL':
        number.append(5)
    elif s in 'MNO':
        number.append(6)
    elif s in 'PQRS':
        number.append(7)
    elif s in 'TUV':
        number.append(8)
    else:
        number.append(9)

total = 0
for num in number:
    total += num+1

print(total)