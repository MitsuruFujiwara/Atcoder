N = int(input())
A = list(map(int,input().split()))

ans = 0
if N == 1:
    print(ans)
else:
    tmp_max = A[0]
    for a in A[1:]:
        if a < tmp_max:
            ans += tmp_max-a
        else:
            tmp_max = a

    print(ans)
