from collections import deque
n=int(input())

graph=[]
max_line=0
for i in range(n):
    temp=list(map(int,input().split()))
    if max_line < max(temp):
        max_line = max(temp)
    graph.append(temp)
dx=[0,0,-1,1]
dy=[1,-1,0,0]
m=0

def bfs(ax,ay):
    q=deque()
    q.append([ax,ay])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx < n and 0<= ny < n and temp[nx][ny]==0:
                temp[nx][ny] = 1
                q.append([nx,ny])





for i in range(101):
    temp = [[0] * n for i in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] <= i:
                temp[j][k] = 1
    for j in range(n):
        for k in range(n):
            if temp[j][k] == 0:
                temp[j][k] = 1
                bfs(j, k)
                cnt += 1

    if cnt == 0:
        break
    m = max(m, cnt)
print(m)




