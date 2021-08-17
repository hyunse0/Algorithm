N = int(input())
total = 0

while N :
    total += N%10
    N //= 10

print(total)