def day_365(month, day) :
    mon = 1

    while mon != month+1 :

        if mon in [2, 4, 6, 8, 9, 11] :
            day += 31
        elif mon == 3 :
            day += 28
        elif mon in [5, 7, 10, 12] :
            day += 30
        
        mon += 1

    return day


T = int(input())

for t in range(1, T+1) :
    month1, day1, month2, day2 = map(int, input().split())
    
    day1 = day_365(month1, day1)
    day2 = day_365(month2, day2)

    print(f'#{t} {day2 - day1 + 1}')