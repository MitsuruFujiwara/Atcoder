A, B, C, D = map(int, input().split())

from math import ceil

if ceil(A/D) >= ceil(C/B):
    print('Yes')
else:
    print('No')
