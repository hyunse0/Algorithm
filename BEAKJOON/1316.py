T = int(input())
cnt = 0

for _ in range(T):
    string = input()

    temp = []
    i = 0
    while i < len(string):
        if string[i] in temp:
            break
        else:
            temp.append(string[i])
            while True:
                if i < len(string)-1 and string[i+1] == temp[-1]:
                    i += 1
                else:
                    break
        
        i += 1

    if i == len(string):
        cnt += 1

print(cnt)