#from collections import deque
n,l=map(int,input().split())
p = list(map(int,input().split()))
p.sort()
start=p[0]
count = 1
for i in p[1:]:
    if i in range(start,start+l):
        continue
    else:
        count+=1
    start=i
print(count)










