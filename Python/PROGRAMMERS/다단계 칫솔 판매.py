# 프로그래머스 다단계 칫솔 판매 -> 틀렸음

from collections import defaultdict

def solution(enroll, referral, seller, amount):
    # 추천인
    recommender = {}
    for i in range(len(enroll)):
        if referral[i] == '-':
            recommender[enroll[i]] = enroll[i]
        else:
            recommender[enroll[i]] = referral[i]
    
    # 본인이 추천한 사람의 수
    recommendee = {}
    for p1, p2 in recommender.items():
        if p1 not in recommendee.keys():
            recommendee[p1] = 0
            
        if p2 not in recommendee.keys():
            recommendee[p2] = 0
            
        while p1 != p2:
            recommendee[p2] += 1
            p1 = p2
            p2 = recommender[p1]
    
    # 추천한 사람이 없는 순서대로 이름 정렬
    names = sorted(recommendee, key=lambda x : recommendee[x])
    
    # 이익
    profit = {}
    for i in range(len(seller)):
        profit[seller[i]] = amount[i]*100
    
    # 최종 이익
    total = defaultdict(int)
    for p in names:
        # 본인의 이익
        sell = 0
        if p in seller:
            sell = profit[p]
        sell += total[p]
        
        # 추천인에게 줄 금액
        temp = int(sell*0.1)
        if p != recommender[p]:
            total[recommender[p]] += temp
        
        # 본인이 가져간 금액
        total[p] = sell - temp
        
    answer = []
    for p in enroll:
        answer.append(total[p])
        
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))