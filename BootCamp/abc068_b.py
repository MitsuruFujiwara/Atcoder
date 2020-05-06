N = int(input())

ans = 1
for i in range(1,8):
    if 2**i > N:
        ans = 2**(i-1)
        break
    elif 2**i == N:
        ans = 2**i
        break

print(ans)
