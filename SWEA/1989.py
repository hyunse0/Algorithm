T = int(input())

for t in range(1, T+1):
    string = input()
    result = 0

    if string == string[::-1]:
        result = 1
    
    print('#{} {}'.format(t, result))