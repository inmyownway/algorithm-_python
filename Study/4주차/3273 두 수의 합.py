from collections import deque
n=int(input())
group=list(map(int,input().split()))
x=int(input())
count=0
group.sort()

i= 0
j = n-1
while i<j:
    temp = group[i]+group[j]
    if temp == x:
        count += 1
        i += 1
        j -= 1
    elif temp >x:
        j -= 1
    elif temp <x:
        i+=1
print(count)


