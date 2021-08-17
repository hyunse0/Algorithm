T = int(input())

for t in range(T) :
    numbers = input()
    numbers = numbers.split()  # 공백 기준으로 잘라서 리스트에 담아줌
    numbers = list(map(int, numbers))

    total = 0

    for num in numbers :
        if num%2 :
            total += num
    
    print(f'#{t+1} {total}')
