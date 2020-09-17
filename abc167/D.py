N, K = map(int, input().split())
A = list(map(int, input().split()))

loc = 0
cnt = 0
towns = [0]
for n in range(N):
    cnt += 1
    loc = A[loc] - 1
    if loc in towns:
        towns.append(loc)
        break
    towns.append(loc)

C = K % cnt
loc = towns[-1]
for c in range(C):
    loc = A[loc] - 1

print(loc+1)
