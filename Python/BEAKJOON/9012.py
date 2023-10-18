# 백준 9012 괄호

def is_VPS(PS):
    temp = []

    for p in PS:
        if p == '(':
            temp.append('(')
        else:
            if not temp:
                return 'NO'

            temp.pop()
    
    if not temp:
        return 'YES'
    
    return 'NO'


T = int(input())

for _ in range(T):
    print(is_VPS(input()))