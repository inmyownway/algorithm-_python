from collections import deque

dx= [0,0,1,-1]
dy= [1,-1,0,0]
n,m=map(int,input().split())
# n 이 가로
# m 이 세로
graph=[]
for i in range(m):
    temp=list(input())
    tl=[]
    for t in temp:
        tl.append(t)
    graph.append(tl)


visited=[[False]*n for _ in range(m)]

def bfs(c,x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    count=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx < m and 0<= ny <n and visited[nx][ny]==False and graph[nx][ny]==c:
                q.append((nx,ny))
                visited[nx][ny]=True
                count+=1
    return count*count

W=0
B=0
for i in range(m):
    for j in range(n):
        if visited[i][j]==False:
            if graph[i][j]=='W':
                W+=bfs('W',i,j)
            elif graph[i][j]=='B':
                B+=bfs('B',i,j)
           #

print(W,B)

