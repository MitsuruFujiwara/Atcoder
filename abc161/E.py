N, K, C = map(int, input().split())
S = input()

ans = []
for i in range(1,N+1,C):
    print(S[i-1])
