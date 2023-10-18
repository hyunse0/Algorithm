def num_to_lst(num):
    string = str(num)
    temp = []

    for s in string:
        temp.append(int(s))

    return temp


def d_sequence(lst):
    d = lst[1] - lst[0]

    for i in range(1, len(lst)-1):
        if num_lst[i+1] - num_lst[i] == d:
            pass
        else:
            return False
    
    return True


N = int(input())

if N < 100:
    cnt = N
else:
    cnt = 99
    for n in range(100, N+1):
        num_lst = num_to_lst(n)

        if d_sequence(num_lst):
            cnt += 1

print(cnt)