N, K = map(int, input().split())

from itertools import combinations
numbers=[]

for n in range(N+1):
    numbers.append(10**100+n)

sums = []
for c in combinations(numbers,K):
    sums.append(c[0]+c[1])

print(len(set(sums)))
