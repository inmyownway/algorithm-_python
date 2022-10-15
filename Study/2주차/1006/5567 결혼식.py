from collections import deque
n=int(input())
l=[[] for _ in range(n+1)]
visited =[False for _ in range(n+1) ]
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    l[x].append(y)
    l[y].append(x)

#[[], [2, 3], [1, 3], [1, 4, 2], [3, 5], [4], []]

count=0
visited[1]=True
for i in l[1]:
    if visited[i]==False:
        visited[i]=True
        count+=1
    for j in l[i]:
            if visited[j]==False:
                visited[j]=True
                count+=1
print(count)



