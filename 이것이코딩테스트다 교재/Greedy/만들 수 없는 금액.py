n=int(input())
data=list(map(int,input().split()))
data.sort()
# 1 2 3 8

target =1
for x in data:
    if target < x:
        break
    target+=x


