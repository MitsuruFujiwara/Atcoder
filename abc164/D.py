S = input()
n = len(S)

ans = 0
for i in range(0,n+1):
    for j in range(i+4,n+1):
        print(S[i:j])
print(ans)
