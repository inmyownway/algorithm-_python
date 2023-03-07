from collections import deque


def bfs(v):
    q=deque()
    q.append(v)
    visited[v]=1
    while q:
        x=q.popleft()

        if x==target:
            return count[target]
        for i in(x+u,x-d):
            if 0<i <=floor and visited[i] ==0:
                visited[i]=1
                q.append(i)
                count[i]=count[x]+1
    if count[target]==0:
        return "use the stairs"


floor,start,target,u,d=map(int,input().split())
visited=[0 for _ in range(floor+1)]
count=[0 for _ in range(floor+1)]
print(bfs(start))
