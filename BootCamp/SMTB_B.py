N = int(input())

from math import floor

ans = 0
for x in range(1,50001):
    if N == floor(x*1.08):
        ans = x

if ans == 0:
    print(':(')
else:
    print(ans)
