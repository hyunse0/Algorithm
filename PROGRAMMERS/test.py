import sys

input =sys.stdin.readline

t = int(input())


for test_case in range(t):
    alphabet_cnt = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,
                    'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,
                    'w':0,'x':0,'y':0,'z':0}
    alphabet_idx = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],
                    'l':[],'m':[],'n':[],'o':[],'p':[],'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],
                    'w':[],'x':[],'y':[],'z':[]}
    str_arr = input()
    k = int(input())

    min_length = 1e12
    max_length = -1
    cnt =0

    for i in str_arr[:-1]:
        alphabet_idx[i].append(cnt)
        alphabet_cnt[i]+=1
        cnt+=1

    alphabet_candidate = ['a','b','c','d','e','f','g','h','i','j','k',
                    'l','m','n','o','p','q','r','s','t','u','v',
                    'w','x','y','z']

    for key,val in alphabet_cnt.items():
        if(val <k):
            alphabet_candidate.remove(key)

    #print(alphabet_candidate)
    # for i in alphabet_candidate:
    #     print(alphabet_idx[i])

    if(len(alphabet_candidate)==0):
        print(-1)
    else:
        for i in alphabet_candidate:
            temp =0
            #print(alphabet_idx[i])
            for j in range(0,len(alphabet_idx[i])-k+1):
                temp = alphabet_idx[i][j+k-1] - alphabet_idx[i][j] +1
                #print(temp,alphabet_idx[i][j],alphabet_idx[i][j+k-1])
                if(temp>max_length and str_arr[alphabet_idx[i][j+k-1]]==str_arr[alphabet_idx[i][j]]):
                    max_length=temp
                if(temp<min_length):
                    min_length =temp

        print(min_length,max_length)