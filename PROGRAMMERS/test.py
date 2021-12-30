from collections import defaultdict

def solution(schedule):
    def select(day):
        nonlocal week

        if len(day) > 8:
            d1, t1, d2, t2 = day.split()

            h1, m1 = t1.split(':')
            h2, m2 = t2.split(':')

            time1 = int(h1)*60 + int(m1)
            time2 = int(h2)*60 + int(m2)

            for _ in range(3):
                if time1 in week[d1]:
                    return False
                
                if time2 in week[d2]:
                    return False

                week[d1].append(time1)
                week[d2].append(time2)
                time1 += 30
                time2 += 30
        else:
            d, t = day.split()
            h, m = t.split(':')
            time = int(h)*60 + int(m)
            for _ in range(6):
                if time in week[d]:
                    return False

                week[d].append(time)
                time += 30
        
        return True

    no = False
    for c1 in schedule[0]:
        week = defaultdict(list)
        can = [[] for _ in range(5)]
        select(c1)
        for c2 in schedule[1]:
            if not select(c2):
                no = True
                break
            else:
                can[1].append()

    answer = -1
    return answer