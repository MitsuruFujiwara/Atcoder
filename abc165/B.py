from math import floor
X = int(input())

amt = 100
ans = 0
while amt < X:
    amt += amt //100
    ans += 1

print(ans)
