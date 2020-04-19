N, M ,C = map(int, input().split())
B = list(map(int,input().split()))

ans = 0

for n in range(N):
    A = list(map(int,input().split()))
    tmp_n = C
    for a,b in zip(A,B):
        tmp_n += a*b

    if tmp_n>0:
        ans +=1

print(ans)
