N = int(input())
S = input()

ans = S.count('R')*S.count('G')*S.count('B')

for i in range(N):
    for j in range(N):
        if i+2*j < N:
            if len(set([S[i],S[i+j],S[i+2*j]]))==3:
                ans -=1
print(ans)
