T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.sort()

    mean = round(sum(numbers[1:9]) / 8)

    print('#{} {}'.format(t, mean))