# 테스트케이스 1~6 틀림

def solution(numbers):
    # 3/30/34를 비교할 경우, 33/30/34를 비교하는 것과 마찬가지
    # [0]이 3일 경우 뒤에 무조건 3이 오므로!
    # 같은 맥락으로 100의 자리일 경우도 고려해서 비어있는 자리를 [0]으로 다 채우기
    temp = {} # {원래 값_개수 : 바뀐 값}
    cnt = 1
    for number in numbers:

        if number < 10:
            if f'{number}_{cnt}' in temp.keys():
                cnt += 1
            temp[f'{number}_{cnt}'] = number*100 + number*10 +number
        elif number < 100:
            if f'{number}_{cnt}' in temp.keys():
                cnt += 1
            temp[f'{number}_{cnt}'] = number*10 + (number//10)
        else :
            if f'{number}_{cnt}' in temp.keys():
                cnt += 1
            temp[f'{number}_{cnt}'] = number
    
    temp_itm = temp.items() # dict_items([('3_1', 333), ('21_1', 212), ('546_1', 546), ('1000_1', 1000)])
    
    # value값을 기준으로 내림차순 정렬
    temp_itm = sorted(temp_itm, key= lambda x : x[1], reverse=True)

    # key만 새로운 리스트에 저장
    temp_key = []

    for key_value in temp_itm:
        temp_key.append(key_value[0].split('_')[0])

    # 만약 temp_key에 1000이 들어가 있다면 0이 없을 경우 제일 뒤,
    # 0이 있을 경우 0의 바로 앞에 위치해야 함
    if '1000' in temp_key:
        temp_key.remove('1000')
        temp_key.append('1000')
    
    if '0' in temp_key:
        temp_key.remove('0')
        temp_key.append('0')

    answer = ''.join(temp_key)

    total = 0
    for ans in answer:
        total += int(ans)
    
    if total == 0:
        answer = '0'

    return answer

numbers = [2, 20, 200]
print(solution(numbers))