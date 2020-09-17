

#==============================================================================
# よく使う処理のメモ
# 参考：https://qiita.com/chun1182/items/ddf2b6cba932b2bb0d4e
#==============================================================================

#二分探索
import bisect
a = [1, 2, 3, 5, 6, 7, 8, 9]
b=bisect.bisect_left(a, 8)

#最大公約数、最小公倍数
import fractions
a,b=map(int, input().split())
f=fractions.gcd(a,b)
f2=a*b//f
print(f,f2)

#combinations、組み合わせ、順列
from itertools import permutations, combinations,combinations_with_replacement,product
a=['a','b','C']
print(list(permutations(a)))
print(list(combinations(a,2)))
print(list(combinations_with_replacement(a,3)))

#集計
from collections import Counter
a=[2,2,2,3,4,3,1,2,1,3,1,2,1,2,2,1,2,1]
a=Counter(a)
for i in a.most_common(3):print(i)
