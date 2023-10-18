N = int(input())
result = []

for n in range(1, N+1):
    number = str(n)
    if '3' in number or '6' in number or '9' in number:
        temp = ''
        for x in number:
            if x in '369':
                temp += '-'
        result.append(temp)
    
    else:
        result.append(number)

print(*result)