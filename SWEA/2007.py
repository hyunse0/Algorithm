T = int(input())

for t in range(1, T+1):
    string = input()
    temp = string[0]

    for i in range(1, 30):
        if string[i] == temp[0]:
            if temp == string[i:i+len(temp)]:
                break
            else:
                temp += string[i]
        else:
            temp += string[i]
    
    print('#{} {}'.format(t, len(temp)))