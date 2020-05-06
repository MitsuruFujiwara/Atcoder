N, K = map(int, input().split())

D =[]
A = []
for k in range(K):
    D.append(int(input()))
    A += list(map(int, input().split()))

print(N - len(set(A)))
