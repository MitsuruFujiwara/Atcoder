A, B, C =map(int, input().split())

ans = 0
if (A==B)&(A==C)&(B==C):
    if A %2==0:
        ans = -1
    else:
        ans = 1
else:
    tmp = (A,B,C)
    while True:
        if (A%2==0)&(B%2==0)&(C%2==0):
            tmp = ((tmp[0]+tmp[1])/2
            A /=2
            B /=2
            C /=2
            ans+=1
        else:
            ans+=1
            break
print(ans)
