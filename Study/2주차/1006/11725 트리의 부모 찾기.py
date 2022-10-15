from collections import deque
n=int(input())

l = [[] for i in range(n+1)]
visited =[False for i in range(n+1)]

for i in range(1,n):

    x,y=map(int,input().split())
    l[x].append(y)
    l[y].append(x)

def bfs(visited,start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        d = q.popleft()
        for i in l[d]:
            if visited[i] == False:
                visited[i] = True

                q.append(i)









