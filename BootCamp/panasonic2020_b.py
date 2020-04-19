H, W = map(int,input().split())
from math import ceil
if W ==1 or H==1:
    print(1)
else:
    print(ceil((W*H)/2))
