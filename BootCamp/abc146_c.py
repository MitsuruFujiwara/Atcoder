A, B, X = map(int, input().split())

import bisect

def price(n):
    return A * n + B*len(str(n))

rng = [price(i) for i in range(10**9)]

ans = bisect.bisect_left(rng, X)
