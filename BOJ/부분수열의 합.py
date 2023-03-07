from itertools import combinations
n,s=map(int,input().split())

l=list(map(int,input().split()))
cnt=0

for i in range(1,n+1):
    temps=list(combinations(l,i))
    for temp in temps:
        print(temp)
        if sum(temp)==s:
            cnt+=1
print(cnt)
