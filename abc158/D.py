S = input()
Q = int(input())

query = []
for q in range(Q):
    query.append(list(input().split()))

is_inv = False

for q in query:
    if q[0] == '1':
        is_inv = ~is_inv
    else:
        if q[1] == '1':
            if is_inv:
                S = S + q[2]
            else:
                S = q[2] + S
        else:
            if is_inv:
                S = q[2] + S
            else:
                S = S + q[2]

if is_inv:
    print(''.join(reversed(list(S))))
else:
    print(S)
