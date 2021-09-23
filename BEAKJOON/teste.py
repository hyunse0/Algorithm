prime = [True for _ in range(10)]

for i in range(2):
    prime[i] = False

for i in range(2, 10):
    temp = i + i
    while temp < 10:
        if prime[temp] == True:
            prime[temp] = False
        
        temp += i

print(prime)