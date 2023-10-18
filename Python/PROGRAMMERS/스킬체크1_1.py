def solution(arr):
    answer = []
    temp = -1
    for number in arr:
        if number != temp:
            answer.append(number)
        temp = number
        
    return answer