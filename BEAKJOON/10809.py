S = input()

alphabet = []
for num in range(ord('a'), ord('z')+1):
    alphabet.append(chr(num))

for a in alphabet:
    end_line = ' '
    if a=='z':
        end_line = '\n'
    
    if a in S:
        print(S.find(a), end=end_line)
    else:
        print(-1, end=end_line)