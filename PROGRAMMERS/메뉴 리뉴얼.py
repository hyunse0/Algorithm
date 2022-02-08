from collections import defaultdict

def solution(orders, course):
    order = defaultdict(list)
    
    for menus in orders:
        for i in range(len(menus)):
            for j in range(i+1, len(menus)):
                order[menus[i]].append(menus[j])
    
    answer = []
    for key, value in order.items():
        for cnt in course:
            temp = [key]
            
            for v in set(value):
                if value.count(v) == cnt:
                    temp.append(v)
            
            if len(temp) >= 2:
                temp.sort()
                answer.append(''.join(temp))
    
    return sorted(list(set(answer)))

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
print(solution(orders, [2, 3, 4]))