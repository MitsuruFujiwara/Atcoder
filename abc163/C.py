N = int(input())
A = list(map(int,input().split()))

from collections import Counter

cnt = Counter(A)

for i in(range(1,N+1)):
    print(cnt[i])
