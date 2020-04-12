import math
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

def comb2(n):
    return n * (n - 1) // 2

c = Counter(A)
ans = 0
for m in c.values():
    if m >= 2:
        ans +=comb2(m)

for i in range(N):
    print(ans - c[A[i]] + 1)
