# 백준 4948 베르트랑 공준

def is_prime_number(number):
    if number == 2:
        return True

    for x in range(2, int(number**0.5) + 1):
        if number%x == 0:
            return False
    
    return True


n = int(input())
while n:
    is_prime = [True for _ in range(2*n+1)]

    is_prime[0] = False
    is_prime[1] = False

    for x in range(2, int((2*n)**0.5) + 1):
        if is_prime[x]:
            if is_prime_number(x):
                mul = 2*x
                while mul <= 2*n:
                    is_prime[mul] = False
                    mul += x

    cnt = 0
    for i in range(n+1, 2*n + 1):
        if is_prime[i]:
            cnt += 1

    print(cnt)

    n = int(input())
