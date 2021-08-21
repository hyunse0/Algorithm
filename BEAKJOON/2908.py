A, B = input().split()

ra = int(A[::-1])
rb = int(B[::-1])

if ra > rb:
    print(ra)
else:
    print(rb)