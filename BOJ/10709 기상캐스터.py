from collections import deque
h,w=map(int,input().split())

result=[[-1]*w for _ in range(h)]


cloud_info=[]
weather=[]
for i in range(h):
    temp=list((input()))
    weather.append(temp)

    for j in range(w):
        if weather[i][j]=='c':
            result[i][j]=0
            cloud_info.append((i,j))

#print(result)
cloud_info.sort()
cloud_info=deque(cloud_info)
#rint("cloud_info",cloud_info)
z=1
#print(result)
while len(cloud_info)>0:


    l=len(cloud_info)
    for i in range(l):
        x,y=cloud_info.popleft()


        #print(x,y)
        if y+1<w:
            if result[x][y+1]==-1:
                result[x][y+1]=z
                cloud_info.append((x,y+1))

        # for a in result:
        #     print(a)
    z+=1


for i in range(h):
    for j in range(w):
        print(result[i][j],end=" ")
    print()