import shlex
from collections import deque
n,m=map(int,input().split())

graph=[]
for i in range(n):
    temp=[]
    t=list(input())

    for j in t:
        temp.append(j)
    graph.append(temp)

distance = [[0]*m for _ in range(n)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
#print(graph)
sonic= deque()
water= deque()
#count=0

DX,DY=0,0
visited=[[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):

        if graph[i][j]=='S':
            sonic.append((i,j))
        elif graph[i][j]=='*':
            water.append((i,j))
        elif graph[i][j]=='X':
            visited=True
        elif graph[i][j]=='D':
            #print(i,j)
            DX=i
            DY=j
count=0

#print(water)
while sonic:

    for i in range(len(water)):
        w_x,w_y = water.popleft()
        visited[w_x][w_y]=True
        #print(w_x,w_y)
        for j in range(4):
            nx= w_x+dx[j]
            ny=w_y +dy[j]
            if 0<= nx < n and 0<= ny < m and graph[nx][ny]!='D':
                #print('hi',nx,ny)
                if graph[nx][ny]!='D' and graph[nx][ny]!='X':
                    #print('aa',nx,ny)
                    graph[nx][ny]='*'
                    water.append((nx,ny))
                    visited[nx][ny]=True
        print(nx,ny)

    x,y=sonic.popleft()
    visited[x][y]=True
    graph[x][y]=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #print(nx,ny)
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]==False \
                and graph[nx][ny]=='.':
            #print(123132)
            graph[nx][ny]=graph[x][y]+1
            visited[nx][ny]=True
            sonic.append((nx,ny))
    for i in graph:
        print(i)
    for j in visited:
        print(j)
    print()
print(graph[DX][DY])



