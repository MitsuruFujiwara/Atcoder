N = int(input())

ans = 0

for n in range(1,N+1):
    if not(n % 3 == 0 or n % 5 == 0):
        ans += n

print(ans)
