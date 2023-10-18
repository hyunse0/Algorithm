string = input()

i = 0
cnt = 0
while i < len(string):
    if i+3 <= len(string) and string[i:i+3] == 'dz=':
        cnt += 1
        i += 3
    elif i+2 <= len(string) and string[i:i+2] in ('c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='):
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

print(cnt)