from collections import deque
r,c,k=list(map(int,input().split()))

camp=[]
for i in range(r):
    temp=list(input().split())
    camp.append(temp)
answer=0
def dfs(sx,sy,goal):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    global answer
    if goal==k:
        if (sx,sy)==(0,c-1):
            answer+=1
    else:
        for i in range(4):
            nx=sx+dx[i]
            ny=sy+dy[i]
            print(nx,ny)
            if 0<= nx < r and 0<= ny <c and camp[nx][ny]!='T':
                camp[nx][ny]='T'
                dfs(nx,ny,goal+1)
                camp[nx][ny]='.'

camp[r-1][0]='T'
dfs(r-1,0,1)
print(answer)