num_list = list(map(int, input().split()))

if (num_list[0] - num_list[1]) == 1 :
    print('A')
elif (num_list[1] - num_list[0]) == 1 :
    print('B')
elif num_list[0] == 1 :
    print('A')
else :
    print('B')