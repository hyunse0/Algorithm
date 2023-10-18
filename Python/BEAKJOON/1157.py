S = input().upper()

cnt = {}
for s in S:
    if s in cnt.keys():
        cnt[s] += 1
    else:
        cnt[s] = 1

max_cnt = max(cnt.values())
max_key = []
for key, value in cnt.items():
    if value == max_cnt:
        max_key.append(key)

if len(max_key) == 1:
    print(max_key[0])
else:
    print('?')