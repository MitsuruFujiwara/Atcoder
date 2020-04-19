N, A, B = map(int, input().split())
S = input()

cnt = 0
cnt_b = 0
for s in S:
    if s =='a':
        if cnt < A+B:
            print('Yes')
            cnt+=1
        else:
            print('No')
    elif s=='b':
        if (cnt < A+B)&(cnt_b < B):
            print('Yes')
            cnt+=1
            cnt_b+=1
        else:
            print('No')
    else:
        print('No')
