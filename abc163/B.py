N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = N-sum(A)

if ans >=0:
    print(ans)
else:
    print('-1')
