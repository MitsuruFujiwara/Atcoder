N = int(input())
A = list(map(int, input().split()))

score_a = 0
score_b = 0

for i, a in enumerate(sorted(A,reverse=True)):
    if i%2==0:
        score_a += a
    else:
        score_b += a
print(score_a-score_b)
