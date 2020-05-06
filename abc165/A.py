K = int(input())
A, B = map(int, input().split())

ans = 'NG'
for n in range(A,B+1):
    if n%K ==0:
        ans = 'OK'

print(ans)
