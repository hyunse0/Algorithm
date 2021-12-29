from itertools import combinations

def solution(prices, d, k):
    prices.sort()

    if prices[-1] - prices[0] <= d:
        return sum(prices)//len(prices)
    
    if prices[-2] - prices[1] <= d:
        return sum(prices[1:-1])//(len(prices)-2)
    
    min_price = float('inf')
    for perm in set(combinations(prices, k)):
        if max(perm) - min(perm) <= d:
            min_price = min(min_price, sum(perm)//k)
        
    if min_price < float('inf'):
        return min_price
    
    if len(prices)//2:
        return prices[len(prices)//2]
    
    return prices[len(prices)//2-1]

prices = [1, 8, 1, 8, 1, 8]
print(solution(prices, 6, 4))