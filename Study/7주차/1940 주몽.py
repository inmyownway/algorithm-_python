
n = int(input())
m = int(input())

l= list(map(int,input().split()))

# 1 2 3 4 5 7
l.sort()

start= 0
end =len(l)-1
count=0

while start < end:

    if l[start]+l[end] == m:
        start+=1
        end-=1
        count+=1
    elif l[start]+l[end] > m:
        end-=1
    elif l[start]+l[end] < m:
        start+=1
print(count)