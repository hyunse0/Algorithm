n1 = int(input())

max_len = 0
max_lst = []

for n2 in range(1, n1+1):
    temp = [n1, n2]

    i = 2
    while True:
        temp_num = temp[i-2] - temp[i-1]
        if temp_num >= 0:
            temp.append(temp_num)
            i += 1
        else:
            if len(temp) > max_len:
                max_len = len(temp)
                max_lst = temp
            
            break

print(max_len)
print(*max_lst)