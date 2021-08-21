def d(n):
    if n < 10:
        return n
    else:
        return d(n//10) + d(n%10)

i = 1
dn_lst = []
while True:
    dn = i + d(i)
    if dn <= 10200:
        dn_lst.append(dn)
        i += 1
    else:
        break

for j in range(1, 10001):
    if j in dn_lst:
        pass
    else:
        print(j)
