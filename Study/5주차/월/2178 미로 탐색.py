from collections import deque
n,m=map(int,input().split())

dx=[0,0,-1,1]
dy=[1,-1,0,0]
graph = []
for i in range(n):
    l=list(map(int,input()))
    graph.append(l)


q= deque()
q.append((0,0))
while q:
    x,y = q.popleft()

    for i in range(4):
        current_x = x+dx[i]
        current_y = y+dy[i]

        if current_x >= n or current_x <0 or current_y >=m or current_y <0:
            continue # 갈수없는 경우
        if graph[current_x][current_y]==0: # 벽인 경우
            continue
        if graph[current_x][current_y]==1:
            q.append((current_x,current_y))
            graph[current_x][current_y]=graph[x][y]+1
print(graph[n-1][m-1])
