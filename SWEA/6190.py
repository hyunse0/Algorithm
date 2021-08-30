T = int(input())

def is_danjo(number):
    temp = []

    while number >= 10:
        temp.append(number%10)
        number //= 10
    
    temp.append(number)

    for i in range(len(temp)-1):
        if temp[i] < temp[i+1]:
            return False
    
    return True


for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    multiple = []
    for i in range(N):
        for j in range(i+1, N):
            multiple.append(numbers[i]*numbers[j])

    max_num = -1
    for number in multiple:
        if is_danjo(number) and number > max_num:
            max_num = number
    
    print('#{} {}'.format(t, max_num))