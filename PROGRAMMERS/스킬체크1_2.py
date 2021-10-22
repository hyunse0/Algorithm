from collections import defaultdict

def factorization(number):
    N = number
    prime_factors = defaultdict(int)

    x = 2
    while x <= N:
        if number%x:
            x += 1
        else:
            prime_factors[x] += 1
            number /= x
    
    return prime_factors


def solution(n, m):
    pf_n = factorization(n)
    pf_m = factorization(m)

    answer = []

    # 최대공약수
    set_n = set(pf_n.keys())
    set_m = set(pf_m.keys())

    ans1 = 1
    for num in set_n&set_m:
        ans1 *= num
    
    answer.append(ans1)

    # 최소 공배수
    ans2 = 1
    
    hap = pf_n
    for num, exponent in pf_m.items():
        hap[num] = max(hap[num], exponent)
    
    for num, exponent in hap.items():
        ans2 *= num**exponent

    answer.append(ans2)    

    return answer

print(solution(3, 5))