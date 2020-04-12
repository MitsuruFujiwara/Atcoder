
from collections import deque

K = int(input())

Q = deque()

for i in range(9):
    Q.append(i+1)
cnt = 0

while cnt < K:
    q = Q.popleft()

    if q % 10 != 0:
        Q.append(10*q+(q%10)-1)

    Q.append(10*q+(q%10))

    if q % 10 != 9:
        Q.append(10*q+(q %10)+1)

    cnt += 1

print(q)
