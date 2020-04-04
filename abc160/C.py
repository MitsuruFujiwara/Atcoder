K, N = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)

max_l = 0
for i　in range(N-1):
  l = A[i+1]-A[i]
  if l > max_l:
    max_l = l



print(max_l)
