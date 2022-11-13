import math
from collections import Counter
n=int(input())

g=[]
for i in range(n):
    g.append(int(input()))

g.sort()

# 산술 평균
print(round(sum(g)/n))

# 중앙값
print(g[n//2])

# 최빈값
max_count = Counter(g)
temp = max_count.most_common() # 빈도수가 작은것부터 (숫자,등장횟수) 로 반환

if len(temp) >1:
    if temp[0][0] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])


# 범위

print(abs(g[-1]-g[0]))


