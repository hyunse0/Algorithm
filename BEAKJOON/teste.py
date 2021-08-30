number = 111566

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

print(is_danjo(number))