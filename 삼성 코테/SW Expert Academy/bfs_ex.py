from collections import deque
n,m=map(int,input().split())

matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().strip())))

print(matrix)
dx=[0,0,-1,1]
dy=[1,-1,0,0]
visited=[[0]*m for _ in range(n)]

count=0
queue=deque()
queue.append([0,0])

while queue:
    x,y=queue.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if x== n-1 and y== m-1:
            #print(matrix[n-1][m-1])
            break

        if 0 <= nx < n and 0<= ny < m:
            #print(nx,ny)
            if visited[nx][ny]==0 and matrix[nx][ny]==1:
                matrix[nx][ny]=matrix[x][y]+1
                visited[nx][ny]=1
                queue.append([nx,ny])
