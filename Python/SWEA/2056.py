T = int(input())

def date(string) :
    year = string[:4]
    month = string[4:6]
    day = string[6:]

    if month in ('01', '03', '05', '07', '08', '10', '12') :
        if int(day) < 1 or int(day) > 31 :
            return -1
        else :
            return f'{year}/{month}/{day}'
    elif month in ('4', '6', '9', '11') :
        if int(day) < 1 or int(day) > 30 :
            return -1
        else :
            return f'{year}/{month}/{day}'
    elif month == '02' :
        if int(day) < 1 or int(day) > 28 :
            return -1
        else :
            return f'{year}/{month}/{day}'

    return -1


for t in range(T) :
    string = input()
    print(f'#{t+1} {date(string)}')