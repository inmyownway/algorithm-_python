n=int(input())
l=list(map(int,input().split()))

dist=[0 for _ in range(len(l))]

#dist[len(l)-1]=0
#for i in range(len(l)-2,-1,-1):

for i in range(0,len(l)-1):
    cnt=0
    for j in range(i+1,len(l)-1):
        #print(l[i],l[j])
        if l[i]>=l[j]:
            cnt+=1
        else:
            cnt+=1
            break
    dist[i]=cnt
print(max(dist))

