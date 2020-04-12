K, N = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)

diff = []
for i, a in enumerate(A[1:]):
    diff.append(a-A[i])

diff.append(K-A[N-1]+A[0])
print(K-max(diff))
