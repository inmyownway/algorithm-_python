from collections import deque


dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    check[x][y]=True
    cnt=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<= nx < n and 0<=ny<m and check[nx][ny]==False and graph[nx][ny]==1:
                cnt+=1
                q.append((nx,ny))
                check[nx][ny]=True
    #print(cnt)
    return cnt


n,m,k=map(int,input().split())

graph=[[0] *m for _ in range(n)]
for i in range(k):
    x,y=map(int,input().split())
    graph[x-1][y-1]=1

check=[[False] * m for _ in range(n)]

max=-1e9

for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and check[i][j]==False:
            temp= bfs(i,j)
            if max < temp:
                max=temp
print(max)