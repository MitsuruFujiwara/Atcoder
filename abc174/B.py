from math import sqrt

N, D = map(int, input().split())

ans = 0
for n in range(N):
    x, y = map(int, input().split())
    l = sqrt(x**2+y**2)
    if l <= D:
        ans +=1

print(ans)
