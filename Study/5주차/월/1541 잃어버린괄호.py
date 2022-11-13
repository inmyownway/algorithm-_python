

n =input().split('-')

l=[]
for i in n:
    m=i.split('+')
    sum=0
    for j in m:
        sum+=int(j)
    l.append(sum)


result=l[0]
for x in range(1,len(l)):
    result -=l[x]
print(result)