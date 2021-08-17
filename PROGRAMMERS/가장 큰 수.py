def solution(numbers):
    lst = []

    for _ in range(len(numbers)):
        temp = ''

        for number in numbers:
            temp += str(number)
        
        lst.append(temp)
        numbers.append(numbers.pop(0))

    print(lst)
    max_num = int(lst[0])

    for num in lst:
        if int(num) > max_num:
            max_num = int(num)
    
    answer = str(max_num)

    return answer

numbers = [6, 10, 2]
print(solution(numbers))