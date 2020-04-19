A = []

for i in range(3):
    a = list(map(int, input().split()))
    A.append(a)

N = int(input())

check = [[0]*3]*3
for n in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                 check[i][j] = 1

ans = 'No'
for i in range(3):
    if check[i][0]+check[i][1]+check[i][2]==3:
        ans = 'Yes'

for i in range(3):
    if check[0][i]+check[1][i]+check[2][i]==3:
        ans = 'Yes'

if check[0][0]+check[1][1]+check[2][2] == 3:
    ans = 'Yes'

if check[0][2]+check[1][1]+check[2][0] == 3:
    ans = 'Yes'

print(ans)
