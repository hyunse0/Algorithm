# 프로그래머스 메뉴 리뉴얼

from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    orders.sort(key=lambda x: -len(x))
    course.sort()

    answer = []
    for cnt in course:
        while orders and len(orders[-1]) < cnt:
            orders.pop()
        
        menus = defaultdict(int)
        for order in orders:
            for combo in combinations(order, cnt):
                combo = sorted(list(combo))
                menus[''.join(combo)] += 1

        result = sorted(menus.items(), key=lambda x: -x[1])
        
        i = 0
        while i < len(result) and result[0][1] >= 2 and result[i][1] == result[0][1]:
            answer.append(result[i][0])
            i += 1
    
    return sorted(answer)

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# print(solution(orders, [2, 3, 4]))

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# print(solution(orders, [2, 3, 5]))

orders = ["XYZ", "XWY", "WXA"]
print(solution(orders, [2, 3, 4]))