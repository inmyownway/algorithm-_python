from itertools import combinations
import sys
n,m=map(int,input().split())

chicken,house = [],[]

for r in range(n):
    data =list(map(int,input().split()))
    for c in range(n):
        if data[c]==1:
            house.append((r,c))
        elif data[c]==2:
            chicken.append((r,c))
candidates=list(combinations(chicken,m))


result = 0

def get_sum(candiate):
    sum=0
    for hx,hy in house:
        temp=1e9
        for cx,cy in candiate:
            temp=min(temp,abs(hx-cx)+abs(hy-cy))
        sum+=temp
    return sum




m=1e9
for candiate in candidates:

    temp= get_sum(candiate)
    m=min(temp,m)
print(m)